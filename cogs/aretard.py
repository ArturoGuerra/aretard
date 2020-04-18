from bot import Plugin, command, guild_only
from random import seed, randint
seed(1)

class Aretard(Plugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.randomstuffs = ["https://media.discordapp.net/attachments/296056831514509312/658820601485459486/video0.mp4", "https://cdn.discordapp.com/attachments/584886538400432154/584890724160503849/Slingshot.mov", "https://media.discordapp.net/attachments/296056831514509312/662123318052257816/oof_2.mp4",
"https://cdn.discordapp.com/attachments/655516260804853791/661806087145783296/video0_2.mp4", "https://cdn.discordapp.com/attachments/655516260804853791/661401266437619742/walter_at_the_bakery_bread1.mp4",
"https://cdn.discordapp.com/attachments/655516260804853791/658939294236540949/canoe.mp4", "https://cdn.discordapp.com/attachments/655516260804853791/657118526737481729/icecream_truck.mp4"]


    @command(name="optimus")
    async def optimus(self, ctx):
        try:
            await ctx.send("https://i.arturonet.com/DTH1pTMnNy.gif")
        except: pass

    @command(name="optimus2")
    async def optimus2(self, ctx):
        try:
            await ctx.send("https://media.discordapp.net/attachments/296056831514509312/680099251258130447/carmechanic.mp4")
        except: pass
    
    @command(name="flips")
    async def flips(self, ctx):
        try:
           await ctx.send("https://tenor.com/view/backflip-back-flip-gif-5547677")
        except: pass

    @command(name="chromie")
    async def chromie(self, ctx):
        try:
           await ctx.send("https://i.arturonet.com/bestvideoever.mp4")
        except: pass

    @command(name="kickme")
    @guild_only()
    async def kickme(self, ctx):
        try:
            await ctx.author.kick()
        except: pass

    @command(name="rhetard")
    async def rhetard(self, ctx):
        try:
            await ctx.send("https://media.discordapp.net/attachments/296056831514509312/699777948575727656/video0.mp4")
        except: pass


    @command(name="cat")
    async def cat(self, ctx):
        try:
            await ctx.send("https://i.redd.it/1e35a6ui9et41.jpg")
        except: pass
        
    @command(name="random")
    async def random(self, ctx):
        max_idx = len(self.randomstuffs) - 1
        idx = randint(0, max_idx)

        try:
            await ctx.send(self.randomstuffs[idx])
        except: pass