import os
import markovify
from glob import glob

class NotReady(Exception):
    pass

class Retard():
    def __init__(self, logger):
        self.models = []
        self.model = None
        self.logger = logger


    def load_models(self):
        files = glob("./models/*.json")
        models = None
        for m in files:
            try:
                with open(m) as f:
                    self.logger.info(f"Loading {m}..")
                    model = markovify.Text.from_json(f.read())
                    if models:
                        models = markovify.combine(models=[models, model])
                    else:
                        models = model
            except Exception as e:
                self.logger.error(f"Error while loading models: {e}")
        self.model = models


    def add_model(self, guild, content):
        try:
            filename = f"./models/{guild}.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            model = markovify.Text(content, state_size=1)
            with open(filename, 'w')  as f:
                f.write(model.to_json())
            self.load_models()
        except Exception as e:
            self.logger.error(e)
        

    def message(self, size):
        if self.model is None:
            raise NotReady

        return self.model.make_short_sentence(size)