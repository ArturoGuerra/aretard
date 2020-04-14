from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self, config, mem_store):
        super().__init__(command_prefix=config.prefix)
        self.config = config
        self.mem_store = mem_store    
