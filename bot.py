# import os
import logging

from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

from translit import translit_dict

logging.basicConfig(level=logging.INFO, filename="mylog.log")

# TOKEN = os.getenv('TOKEN')

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
    translit_list = []
    for w in text.lower():
        try:
            translit_list.append(translit_dict[w])
        except:
            translit_list.append(w)
            
    translit_list = "".join(translit_list)

    logging.info(f'{user_name=} {user_id=} sent message: {translit_list}')
    await bot.send_message(user_id, translit_list)


if __name__ == '__main__':
    executor.start_polling(dp)
