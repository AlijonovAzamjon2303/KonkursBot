from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_admin_menu():
    button1 = KeyboardButton(text="Kanal qo'shish")
    button2 = KeyboardButton(text="Barcha kanallar")

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [button1],
            [button2]
        ],
        resize_keyboard=True
    )

    return keyboard

def get_cancel_button():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bekor qilish")]
        ],
        resize_keyboard=True
    )

    return keyboard