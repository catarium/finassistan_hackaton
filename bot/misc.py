from apscheduler.schedulers.asyncio import AsyncIOScheduler
from tortoise import Tortoise
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from bot.core.config import config
from bot.services.auto_news import Notifier

storage = RedisStorage2(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
)
bot = Bot(token=config.TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=storage)


async def database_init():
    db_url = f'postgres://{config.POSTGRES_USER}:' \
          f'{config.POSTGRES_PASSWORD}@' \
          f'{config.POSTGRES_HOST}:' \
          f'{config.POSTGRES_PORT}/' \
          f'{config.POSTGRES_NAME}'
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['bot.db.models']}
    )


notifier = Notifier(AsyncIOScheduler(), bot)


def setup():
    import bot.handlers.home
    import bot.handlers.finances
    import bot.handlers.calculator
    import bot.handlers.admin
