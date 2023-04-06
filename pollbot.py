import asyncio
import logging
import os

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def start_poll():
    # Создание опроса
    poll = types.Poll(
        question="Как вам наш продукт?",
        options=["Отлично", "Хорошо", "Удовлетворительно"],
        is_anonymous=False
    )

    # Отправка опроса в чат
    await bot.send_poll(chat_id="CHAT_ID", poll=poll)


# Запуск голосования каждую минуту
async def schedule_poll():
    while True:
        await start_poll()
        await asyncio.sleep(60)


# Добавление задачи в цикл событий
async def on_startup(dp):
    asyncio.create_task(schedule_poll())


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)