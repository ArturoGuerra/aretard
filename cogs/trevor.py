from bot import Plugin, command, listener
import markovify
import discord

class Trevor(Plugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.messages = []
        self.text = None

    def toChain(self):
        text = ""
        for m in self.messages:
            text += m + "\n"

        if len(text) > 0:
            self.text = markovify.NewlineText(text, state_size=1)

    def newMessage(self):
        if self.text is None:
            self.toChain()
            return "Sorry looks like im not retarded enough yet"

        return self.text.make_short_sentence(2000)

    @listener()
    async def on_ready(self):
        if len(self.messages) > 0:
            return

        print("Retardifing...")
        channels = []

        for channel in self.bot.get_all_channels():
            if type(channel) is discord.TextChannel:
                channels.append(channel)

        for channel in channels:
            try:
                messages = await channel.history(limit=10000).flatten()
                count = 0
                for m in messages:
                    if m.content != "" and not m.author.bot and self.bot.config.prefix not in m.content:
                        count += 1
                        self.messages.append(m.content)
                print(f"Processed {count} messages from {channel.name}:{channel.id}")
                self.toChain()
            except Exception as e:
                print(f"Error processing channel: {channel.name} {e}")
        print('Done processing channels')
        self.toChain()
        
    @listener()
    async def on_message(self, message):
        if not message.content.startswith(self.bot.config.prefix):
            self.messages.append(message.content)
            self.toChain()

    @listener()
    async def on_guild_join(self, guild):
        channels = []

        for channel in guild.channels:
            if type(channel) == discord.TextChannel:
                channels.append(channel)
        
        for channel in channels:
            try:
                messages = await channel.history(limit=10000).flatten()
                count = 0
                for m in messages:
                    if m.content != "" and not m.author.bot and self.bot.config.prefix not in m.content:
                        count += 1
                        self.messages.append(m.content)
                print(f"Processed {count} messages from {channel.name}:{channel.id}")
            except Exception as e:
                print(f"Error processing channel: {channel.name} {e}")
        print('Done processing channels')
        self.toChain()


    @command(name='retard')
    async def retard(self, ctx):
        message = self.newMessage()
        try:
            await ctx.send(message)
        except Exception as e:
            print(e)