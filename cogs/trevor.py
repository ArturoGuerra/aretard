from bot import Plugin, command, listener, is_owner, guild_only, retarded_servers
import retarder
import discord

class Trevor(Plugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.markov = retarder.Retard(bot.logger)

    @listener()
    async def on_ready(self):
        self.logger.info("Loading markov models...")
        self.markov.load_models()

    @command(name='retard')
    @guild_only()
    @retarded_servers()
    async def retard(self, ctx):
        try:
            message = self.markov.message(200)
            await ctx.send(message.replace('@everyone', "@ everyone").replace("@here", "@ here"))
        except Exception as e:
            self.logger.error(e)
    
    @command(name="newmodel", hidden=True)
    @guild_only()
    @is_owner()
    async def newmodel(self, ctx):
        text = ""
        channels = []

        for channel in ctx.guild.channels:
            if type(channel) == discord.TextChannel:
                channels.append(channel)

        for channel in channels:
            try:
                self.logger.info(f"Adding channel content for: {channel.name}:{channel.id}")
                messages = await channel.history(limit=10000).flatten()
                for m in messages:
                    if m.content != "" and self.bot.config.prefix not in m.content:
                        text += m.content + "\n"
            except Exception as e:
                self.logger.error(e)

        if text != "":
            self.markov.add_model(ctx.guild.id, text)
        
        self.logger.info(f"Done processing {ctx.guild.name}:{ctx.guild.id}")