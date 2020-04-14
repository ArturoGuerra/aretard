import os


import discord
from random import seed,randint
seed(1)

wierdShit = ["https://cdn.discordapp.com/attachments/584886538400432154/584890724160503849/Slingshot.mov", "https://media.discordapp.net/attachments/296056831514509312/662123318052257816/oof_2.mp4",
"https://cdn.discordapp.com/attachments/655516260804853791/661806087145783296/video0_2.mp4", "https://cdn.discordapp.com/attachments/655516260804853791/661401266437619742/walter_at_the_bakery_bread1.mp4",
"https://cdn.discordapp.com/attachments/655516260804853791/658939294236540949/canoe.mp4", "https://cdn.discordapp.com/attachments/655516260804853791/657118526737481729/icecream_truck.mp4"]


token = 'Njc2MjA3MDc3MDEzNTg1OTUx.XmSSOw.7gbKDICAzYOKTiM2uc4bC014JpM'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is retarded')

@client.event
async def on_message(lmao):
    if lmao.content.lower() == "!aretard":
        await lmao.channel.send("https://tenor.com/view/backflip-back-flip-gif-5547677")

    elif lmao.content.lower() == "!optimus":
        await lmao.channel.send("https://i.arturonet.com/DTH1pTMnNy.gif")

    elif lmao.content.lower() == "!chromie":
        await lmao.channel.send("https://i.arturonet.com/bestvideoever.mp4")

    elif lmao.content.lower() == "!kickme":
         print("retard")
         await lmao.guild.kick(lmao.author)

    elif lmao.content.lower() == "!random":
        await lmao.channel.send("https://i.arturonet.com/bestvideoever.mp4")





client.run(token)
