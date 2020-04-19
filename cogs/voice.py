from bot import Plugin, command, guild_only
import discord

class Voice(Plugin):
    def __init__(self, bot):
        super().__init__(bot)

    def getLink(self, query):
        if query.startswith("http"):
            return query
        
        return f"ytsearch:{query}"

    @command(name="connect", aliases=["join"])
    @guild_only()
    async def connect_(self, ctx, channel: discord.VoiceChannel=None):
        if not channel:
            try:
                channel = ctx.author.voice.channel
            except:
                return
        
        try:
            player = self.bot.wavelink.get_player(ctx.guild.id)
            await player.connect(channel.id)
        except Exception as e:
            print(e)
            self.bot.logger.error(e)

    @command(name="play", aliases=["p"])
    @guild_only()
    async def play(self, ctx, *, query: str):
        if query is None:
            return

        item = self.getLink(query)

        tracks = await self.bot.wavelink.get_tracks(item)

        if not tracks:
            try:
                await ctx.send("Unable to play song")
            except:
                return
        
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_connected:
            try:
                await ctx.invoke(self.connect_)
            except Exception as e:
                print(e)
                return

        try:
            await player.play(tracks[0])
            await ctx.send(f"Playing {tracks[0]}")
        except Exception as e:
            self.bot.logger.error(e)

    @command(name="leave", aliases=['disconnect'])
    @guild_only()
    async def leave(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            await player.disconnect()
            await ctx.send("I have disconnected")
        except Exception as e:
            print(e)

    @command(name="stop")
    @guild_only()
    async def stop(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            await player.stop()
        except Exception as e:
            print(e)

    @command(name="pause")
    @guild_only()
    async def pause(self, ctx):
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            playing = not player.is_playing
            await player.set_pause(playing)
            await ctx.send(f"Paused/Unpaused player")
        except Exception as e:
            self.bot.logger.error(e)

    @command(name="vol", aliases=['volume'])
    @guild_only()
    async def volume_(self, ctx, vol: int):
        if vol is None:
            return

        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            await player.set_volume(vol)
            await ctx.send(f"Set volume to {vol}")
        except Exception as e:
            self.bot.logger.error(e)

    @command(name="ree")
    @guild_only()
    async def ree(self, ctx):
        try:
            await self.play(ctx, query = "reee")
        except Exception as e:
            self.logger.error(e)

    @command(name='chromie2')
    @guild_only()
    async def chromie2(self, ctx):
        try:
            await self.play(ctx, query = "https://i.arturonet.com/bestvideoever.mp4")
        except Exception as e:
            self.logger.error(e)
        
            

