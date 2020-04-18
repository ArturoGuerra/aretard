from bot import Plugin, command, listener

class General(Plugin):
    def __init__(self, bot):
        super().__init__(bot)

    @command(name="addme")
    async def addme(self, ctx):
        try:
            await ctx.send("https://discordapp.com/oauth2/authorize?client_id=700960910201585704&scope=bot&permissions=117760")
        except: pass
    