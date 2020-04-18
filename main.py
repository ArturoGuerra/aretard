from bot import Bot, Config
from stores import MemStore

from cogs import register

import asyncio
import logging

# Makes use a uvloop which is written is C for much better performance
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger = logging.getLogger('aretard')
logger.addHandler(sh)
logger.setLevel(logging.INFO)

logger.info(f"Starting aretard :)")

config = Config.Create()
mem_store = MemStore()
bot = Bot(config, logger, mem_store)
register(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.set_debug(True)

    bot.loop = loop

    try:
        loop.run_until_complete(bot.start(bot.config.token, reconnect=True))
    except KeyboardInterrupt:
        loop.run_until_complete(bot.logout())
    finally:
        loop.close()