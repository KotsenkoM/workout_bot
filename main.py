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
    answer = ['Иду', 'Пас']
    await bot.send_poll(chat_id=CHAT_ID, question='Выходим через 5 минут?', options=answer, is_anonymous=False)


async def start_poll_soup_and_workout():
    """
    Создает голосование в телеграм чате
    """
    answer = [
        'Иду',
        'Возьмите мне супчика плез',
        'Пас'
    ]
    now = datetime.now()
    # Получаем день недели (понедельник - 0, воскресенье - 6)
    day_of_week = now.weekday()

    soup_dict = {
        0: "Борщч",
        1: "Горох",
        2: "Лапша",
        3: "Опять борщч",
        4: "Рассольник"
    }
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=f'Го за супчиком в 11? Сегодня {soup_dict[day_of_week]}',
        options=answer,
        is_anonymous=False
    )


async def start_poll_where_to_go():
    """
    Создает голосование в телеграм чате
    """
    answer = [
        'Я за супчиком, завтра борщч',
        'Го в таракальную',
        'Го в атриум',
        'Го за шавой',
        'Го в милти',
        'Го в тануки'
        'Напишу свой вариант ниже',
        'У меня с собой'
    ]
    await bot.send_poll(
        chat_id=CHAT_ID,
        question='Го куда-нибудь завтра?',
        options=answer,
        is_anonymous=False,
        allows_multiple_answers=True
    )


async def start_poll_sirniki_time():
    answer = [
        'Я все куплю!',
        'Сырники (80руб)',
        'Сырники 2 порции (160руб)',
        'Запеканка (140руб)',
        'Сметана (15руб)',
        'Джем (15руб)',
        'какИра (бесценно)',
        'Сам возьму',
        'Другое, напишу ниже',
        'Ничего не буду, спасибо'
    ]
    await bot.send_poll(
        chat_id=CHAT_ID,
        question='Го в столовку?',
        options=answer,
        is_anonymous=False,
        allows_multiple_answers=True
    )


async def start_poll_dinner_time():
    """
    Создает голосование в телеграм чате
    """
    answer = ['Го в 12:30', 'Го в 13:00', 'Го в 13:30', 'Пас']
    await bot.send_poll(chat_id=CHAT_ID, question='Во сколько на обед сегодня?', options=answer, is_anonymous=False)

if __name__ == '__main__':
    scheduler.add_job(start_poll_workout, 'cron', day_of_week='mon-fri', hour='10, 15', minute='55')
    scheduler.add_job(start_poll_sirniki_time, 'cron', day_of_week='mon-fri', hour='08', minute='45')
    scheduler.add_job(start_poll_where_to_go, 'cron', day_of_week='wed', hour='20', minute='00')
    scheduler.add_job(
        start_poll_soup_and_workout,
        'cron',
        day_of_week='mon, tue, wed, fri',
        hour='10',
        minute='00'
    )
    scheduler.add_job(start_poll_dinner_time, 'cron', day_of_week='mon-fri', hour='11', minute='45')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
