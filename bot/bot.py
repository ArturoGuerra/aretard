from discord.ext import commands
import wavelink
import uuid

class Bot(commands.Bot):
    def __init__(self, config, logger, mem_store):
        super().__init__(command_prefix=config.prefix)
        self.config = config
        self.logger = logger
        self.mem_store = mem_store
        self.wavelink = None
    
    async def on_ready(self):
        self.logger.info("Aretard is ready...")
        if self.wavelink == None:
            await self.start_wavelink()
        

    async def start_wavelink(self):
        id = uuid.uuid1()
        self.wavelink = wavelink.Client(self)
        if self.config.voice_enabled:
            await self.wavelink.initiate_node(host=self.config.lavalink_host,
                                          port=self.config.lavalink_port,
                                          rest_uri=self.config.lavalink_uri,
                                          password=self.config.lavalink_password,
                                          identifier=f'aretard-{id}',
                                          region='us_central')