from bot import Plugin, command, listener

class General(Plugin):
    def __init__(self, bot):
        super().__init__(bot)

    @listener()
    async def on_ready(self):
        print(f"Project Retard has started..")

    @command(name="addme")
    async def addme(self, ctx):
        try:
            await ctx.send("https://discordapp.com/oauth2/authorize?client_id=676207077013585951&scope=bot&permissions=117760")
        except: pass
    