import os
import markovify
from io import BytesIO
from minio import Minio
import threading

class NotReady(Exception):
    pass

class RetardConfig():
    def __init__(self, prefix=None):
        self.host = os.getenv("S3_HOST")
        self.access_key = os.getenv("S3_ACCESS_KEY")
        self.secret_key = os.getenv("S3_SECRET_KEY")
        self.bucket = os.getenv("S3_BUCKET")
        self.prefix = prefix
        self.secure = True

class Retard():
    def __init__(self, logger, config):
        self.models = []
        self.model = None
        self.logger = logger
        self.config = config
        self.minio = Minio(config.host,
            access_key=config.access_key,
            secret_key=config.secret_key,
            secure=config.secure)

    def __get_model_data(self, object):
        data = self.minio.get_object(object.bucket_name, object.object_name.encode("utf-8"))
        return b"".join(data.stream(32*1024))

    def __get_models_data(self):
        items = []
        
        objects = self.minio.list_objects(self.config.bucket, prefix=self.config.prefix)
        for obj in objects:
            if not obj.is_dir and obj.object_name.endswith(".json"):
                try:
                    self.logger.info(f"Getting model data for: {obj.object_name}")
                    item = self.__get_model_data(obj)
                    items.append(item)
                except Exception as e:
                    self.logger.error(e)

        return items

    def load_models(self):
        t = threading.Thread(target=self.__load_models)
        t.start()

    def __load_models(self):
        data = self.__get_models_data()
        models = None
        for m in data:
            try:
                model = markovify.NewlineText.from_json(m)
                if models:
                    models = markovify.combine(models=[models, model])
                else:
                    models = model
            except Exception as e:
                self.logger.error(f"Error while loading models: {e}")
        self.logger.info(f"Done loading models {self.config.prefix}")
        self.model = models

    def add_model(self, guild, content):
        try:
            model = markovify.NewlineText(content, state_size=1)
            filename = f"{self.config.prefix}-{guild}.json"
            bcontent = BytesIO(bytes(model.to_json(), 'utf-8'))
            size = bcontent.getbuffer().nbytes

            try:
                self.minio.put_object(self.config.bucket, filename, bcontent, size)
                self.load_models()
            except Exception as e:
                self.logger.error(e)

        except Exception as e:
            self.logger.error(e)
        

    def message(self, size):
        if self.model is None:
            raise NotReady

        return self.model.make_short_sentence(size)