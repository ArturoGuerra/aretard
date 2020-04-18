#We Wide BOIS
from .general import General
from .aretard import Aretard
from .trevor  import Trevor
from .voice   import Voice

def register(bot):
    bot.add_cog(General(bot))
    bot.add_cog(Aretard(bot))
    bot.add_cog(Trevor(bot))
    if bot.config.voice_enabled:
       bot.add_cog(Voice(bot))