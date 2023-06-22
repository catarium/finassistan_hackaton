import random

from aiogram import Bot

from bot.db.models import Advice, User
from tortoise.contrib.postgres.functions import Random


async def daily_advice(bot: Bot):
    advices = await Advice.all()
    if not advices:
        return
    advice = random.choice(advices)
    for user in (await User.all()):
        msg = f'''
Совет дня:        
{advice}
'''
        try:
            await bot.send_message(user.telegram_id, advice.content)
        except:
            pass
