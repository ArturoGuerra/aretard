from discord.ext import commands
import os

class NoPrivateMessages(commands.CheckFailure):
    pass

class NotAnOwner(commands.CheckFailure):
    pass

class NotInGuild(commands.CheckFailure):
    pass

def guild_only():
    async def predicate(ctx):
        if ctx.guild is None:
            raise NoPrivateMessages('Hey no DMs!')
        return True
    return commands.check(predicate)

owners = ['411323761116184578']

def is_owner():
    async def predicate(ctx):
        if ctx.author.id in owners:
            raise NotAnOwner("Hey you are not an owner")
        return True
    return commands.check(predicate)

retards = os.getenv("RETARDED_SERVERS").split(',')

def retarded_servers():
    async def predicate(ctx):
        if ctx.guild.id in retards:
            raise NotInGuild("Looks you are not allowed to use this command")
        return True
    return commands.check(predicate)