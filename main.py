import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.core.config import config
from bot.misc import database_init, dp, bot, setup
# import aioschedule as schedule

logger = logging.getLogger(__name__)


async def main():
    setup()
    await database_init()
    await dp.start_polling()

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")