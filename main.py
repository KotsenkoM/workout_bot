import logging
import os

from aiogram import Bot, Dispatcher, executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
QUESTION = os.getenv('QUESTION')
OPTIONS = os.getenv('OPTIONS')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()


async def start_poll():
    """
    Создает голосование в телеграм чате
    """
    await bot.send_poll(chat_id=CHAT_ID, question=QUESTION, options=OPTIONS.split(', '), is_anonymous=False)


if __name__ == '__main__':
    scheduler.add_job(start_poll, 'cron', day_of_week='mon-fri', hour='10, 15', minute='55')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
