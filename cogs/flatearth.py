from bot import Plugin, command, listener, is_owner, guild_only, retarded_servers
import retarder
import discord

class FlatEarth(Plugin):
    def __init__(self, bot):
        super().__init__(bot)
        config = retarder.RetardConfig("fe")
        self.markov = retarder.Retard(bot.logger, config)

    @listener()
    async def on_ready(self):
        self.logger.info("Loading markov models...")
        self.markov.load_models()

    @command(name='fe')
    @guild_only()
    @retarded_servers()
    async def retard(self, ctx):
        try:
            message = self.markov.message(200)
            await ctx.send(message.replace('@everyone', "@ everyone").replace("@here", "@ here"))
        except Exception as e:
            self.logger.error(e)