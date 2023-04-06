import logging
import os
import schedule
import datetime
import time

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет')


# @dp.message_handler(commands=['poll'])
async def start_poll(bot: Bot, chat_id: int):
    question = 'Го на турнички'
    options = ['го', 'нет']
    await bot.send_poll(chat_id=chat_id, question=question, options=options, is_anonymous=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
