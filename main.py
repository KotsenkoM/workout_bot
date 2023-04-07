import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start_poll():
    question = 'Го на турнички'
    options = ['го', 'нет']
    while True:
        await bot.send_poll(chat_id=CHAT_ID, question=question, options=options, is_anonymous=False)
        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.get_event_loop().create_task(start_poll())
    executor.start_polling(dp, skip_updates=True)
