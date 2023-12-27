import logging
import os

from aiogram import Bot, Dispatcher, executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()


async def start_poll_workout():
    """
    Создает голосование в телеграм чате
    """
    answer = ['Иду', 'Пропускаю']
    await bot.send_poll(chat_id=CHAT_ID, question='Го на турнички через 5 минут?', options=answer, is_anonymous=False)


async def start_poll_soup():
    """
    Создает голосование в телеграм чате
    """
    answer = ['Иду', 'Пас']
    now = datetime.now()
    # Получаем день недели (понедельник - 0, воскресенье - 6)
    day_of_week = now.weekday()

    soup_dict = {
        0: "Борщч",
        1: "Горох",
        2: "Лапша",
        3: "ХИНКАЛИ! Ну а в кофепорте опять борщч",
        4: "Рассольник"
    }
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=f'Го за супчиком? Сегодня {soup_dict[day_of_week]}',
        options=answer,
        is_anonymous=False
    )


async def start_poll_khinkali():
    """
    Создает голосование в телеграм чате
    """
    answer = ['Го в 12:30', 'Го в 13:00', 'Го в 13:30', 'Пас']
    await bot.send_poll(chat_id=CHAT_ID, question='Го в хинкальную сегодня?', options=answer, is_anonymous=False)

if __name__ == '__main__':
    # scheduler.add_job(start_poll_workout, 'cron', day_of_week='mon-fri', hour='10, 15', minute='55')
    scheduler.add_job(start_poll_soup, 'cron', day_of_week='mon-fri', hour='10', minute='00')
    scheduler.add_job(start_poll_khinkali, 'cron', day_of_week='thu', hour='11', minute='30')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
