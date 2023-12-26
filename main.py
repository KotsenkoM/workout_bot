import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
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


# @dp.message_handler(commands=['what'])
# async def start_command(message: types.Message):
#     # Получите ID группового чата
#     chat_id = message.chat.id
#     await message.reply(f"ID группового чата: {chat_id}")


# async def pdr_search():
#     await bot.send_message(chat_id=CHAT_ID, text='/pidoreg@SublimeBot')



if __name__ == '__main__':
    scheduler.add_job(start_poll_workout, 'cron', day_of_week='mon-fri', hour='10, 15', minute='55')
    # scheduler.add_job(pdr_search, 'cron', hour='15', minute='34')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
