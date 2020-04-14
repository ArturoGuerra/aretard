import os

class Config:
    def __init__(self, token, prefix):
        self.prefix = prefix
        self.token = token
    
    @staticmethod
    def Create():
        token = os.getenv('TOKEN')
        prefix = os.getenv('PREFIX')

        if prefix is None:
            prefix = '!'

        return Config(token, prefix)