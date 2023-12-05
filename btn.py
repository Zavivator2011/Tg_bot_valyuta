from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def valyuta_btn(data):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn.add(
        *[KeyboardButton(f"{item['code']}") for item in data]
    )

    return btn