from bot import Plugin, command, listener

class General(Plugin):
    def __init__(self, bot):
        super().__init__(bot)

    @listener()
    async def on_ready(self):
        print(f"Project Retard has started..")
    