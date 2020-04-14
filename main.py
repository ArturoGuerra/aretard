from bot import Bot, Config
from stores import MemStore

from cogs import register

config = Config.Create()
mem_store = MemStore()
bot = Bot(config, mem_store)

register(bot)

if __name__ == "__main__":
    try:
        bot.loop.run_until_complete(bot.start(bot.config.token, reconnect=True))
    except KeyboardInterrupt:
        bot.loop.run_until_complete(bot.logout())
    finally:
        bot.loop.close()