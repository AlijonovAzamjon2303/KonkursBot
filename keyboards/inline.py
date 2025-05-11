from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from database.admin import get_all_chanels

def get_all_chanel_keyboard():
    all_chanels = get_all_chanels()
    chanels_inline_buttons = []

    for chanel in all_chanels:
        inline_button = [InlineKeyboardButton(text=chanel[1], callback_data=f"chanel_{chanel[0]}")]
        chanels_inline_buttons.append(inline_button)

    return InlineKeyboardMarkup(inline_keyboard=chanels_inline_buttons)