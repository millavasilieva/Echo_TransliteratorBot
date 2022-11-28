import os
import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN

import transliterate
from transliterate import translit

logging.basicConfig(level=logging.INFO, filename="mylog.log")

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f"Здравствуй, {user_name}! Напиши свое полное имя (ФИО)."

    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_message(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    text = text.lower().replace('ь', '').replace('я', 'иа').replace('щ', 'шч').replace('й', 'и').replace('ъ', 'ие').replace('х', 'кх').replace('ю', 'иу')
    text = " ".join([i.upper() for i in text.split(" ")])
    text = translit(text, language_code='ru', reversed=True)

    logging.info(f'{user_name=} {user_id=} sent message: {text}')
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)
