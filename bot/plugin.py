from .bot import Bot
from discord.ext.commands import Cog


class Plugin(Cog):
    def __init__(self, bot):
        self.bot = bot