from tortoise import Tortoise
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from bot.core.config import config

storage = RedisStorage2(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    # db=config.REDIS_DB
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


def setup():
    import bot.handlers.home