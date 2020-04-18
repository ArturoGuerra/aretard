from .bot import Bot
from .config import Config
from .plugin import Plugin
from .checks import guild_only, is_owner, retarded_servers

from discord.ext.commands import command, Cog

listener = Cog.listener