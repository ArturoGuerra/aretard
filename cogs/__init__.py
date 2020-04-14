#We Wide BOIS
from .general import General
from .aretard import Aretard
from .trevor  import Trevor

def register(bot):
    bot.add_cog(General(bot))
    bot.add_cog(Aretard(bot))
    bot.add_cog(Trevor(bot))