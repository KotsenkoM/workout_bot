import logging
import os

import schedule
import datetime

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start_poll():
    question = 'Го на турнички'
    options = ['Вариант 1', 'Вариант 2', 'Вариант 3']
    await bot.send_poll(chat_id=CHAT_ID, question=question, options=options)


def job():
    now = datetime.datetime.now()
    if now.weekday() < 5:
        dp.loop.create_task(start_poll())


schedule.every(3).seconds.do(start_poll)

while True:
    schedule.run_pending()

