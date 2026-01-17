# pip install aiogram

import time

from aiogram import Bot, Dispatcher, Command

token = "8219796564:AAGNJG9X_wXmxRYVrH-PHTPhqq7eTo1YpWg"

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
  await message.answer("Hello!")


async def main():
  try:
    print("Bot running")
    await dp.start_polling(bot)
  except Exception as e:
    print(f"ERROR: {e}")
    time.time(20)
