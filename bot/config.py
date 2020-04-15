import os

class Config:
    def __init__(self, token, prefix, lavalink_host, lavalink_port, lavalink_uri, lavalink_password):
        self.prefix = prefix
        self.token = token
        self.lavalink_host = lavalink_host
        self.lavalink_port = lavalink_port
        self.lavalink_uri  = lavalink_uri
        self.lavalink_password = lavalink_password
    
    @staticmethod
    def Create():
        token = os.getenv('TOKEN')
        prefix = os.getenv('PREFIX')
        lavalink_host = os.getenv("LAVALINK_HOST")
        lavalink_port = os.getenv("LAVALINK_PORT")
        lavalink_uri  = os.getenv("LAVALINK_URI")
        lavalink_password = os.getenv("LAVALINK_PASSWORD")

        if prefix is None:
            prefix = '!'

        return Config(token, prefix, lavalink_host, lavalink_port, lavalink_uri, lavalink_password)