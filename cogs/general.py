from bot import Plugin, command, listener

class General(Plugin):
    def __init__(self, bot):
        super().__init__(bot)

    @command(name="creator")
    async def creator(self, ctx):
        try:
            await ctx.send("https://streamable.com/d5pfi")
        except: pass

    @command(name="addme")
    async def addme(self, ctx):
        try:
            await ctx.send(f"https://discordapp.com/oauth2/authorize?client_id={self.bot.user.id}&scope=bot&permissions=117760")
        except: pass
    