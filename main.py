import logging
import os

from aiogram import Bot, Dispatcher, executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()


async def start_poll():
    """
    Создает голосование в телеграм чате
    """
    question = 'Го на турнички через 5 минут?'
    options = ['Иду', 'Пропускаю']
    await bot.send_poll(chat_id=CHAT_ID, question=question, options=options, is_anonymous=False)


if __name__ == '__main__':
    scheduler.add_job(start_poll, 'cron', day_of_week='mon-fri', hour='10, 15', minute='55')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
