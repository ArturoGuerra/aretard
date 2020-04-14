from bot import Bot, Config
from stores import MemStore

from cogs import register

import asyncio

# Makes use a uvloop which is written is C for much better performance
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

config = Config.Create()
mem_store = MemStore()
bot = Bot(config, mem_store)

register(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_debug(True)

    bot.loop = loop
    
    try:
        loop.run_until_complete(bot.start(bot.config.token, reconnect=True))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.logout())
    finally:
        loop.close()