#We Wide BOIS
from .general import General
from .aretard import Aretard

def register(bot):
    bot.add_cog(General(bot))
    bot.add_cog(Aretard(bot))