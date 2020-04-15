from discord.ext import commands
import wavelink

class Bot(commands.Bot):
    def __init__(self, config, logger, mem_store):
        super().__init__(command_prefix=config.prefix)
        self.config = config
        self.logger = logger
        self.mem_store = mem_store
        self.wavelink = wavelink.Client(self)
    
    async def on_ready(self):
        self.logger.info("Starting wavelink...")
        await self.wavelink.initiate_node(host=self.config.lavalink_host,
                                          port=self.config.lavalink_port,
                                          rest_uri=self.config.lavalink_uri,
                                          password=self.config.lavalink_password,
                                          identifier='aretard',
                                          region='us_central')