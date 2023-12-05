import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command

from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from btn import *
from untils import *

BOT_TOKEN = "6502882014:AAE31XBkaUL1HrUh4E1Wb7VwmbiGXDdLGQ8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

ADMINS = [591250245, 234234235]


async def command_menu(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Ishga tushirish'),
        ]
    )


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    data = await get_current_data()
    btn = await valyuta_btn(data)
    await message.answer("Menda eng yaxshi valyuta kurslari mavjud",reply_markup=btn)



@dp.message_handler(content_types=['text'])
async def get_valyuta_handler(message: types.Message):
    text = message.text
    data = await get_current_data()
    check_text = await check_btn_text(data, text)
    if check_text:
        context = await make_data_context(data, text)
        await message.answer(context)
    else:
        await message.answer(f"Bizda {text} nomli valyuta mavjud emas!")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=command_menu)
