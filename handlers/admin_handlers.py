from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from database.admin import add_chanel_to_db
from config import ADMINS
from keyboards.inline import get_all_chanel_keyboard
from keyboards.reply import get_cancel_button, get_admin_menu
from states.admin_states import AddChanel

router = Router()

@router.message(F.text == "Barcha kanallar")
async def get_all_chanel(message:Message):
    if message.from_user.id in ADMINS:
        await message.answer("Hurmatli admin sizning kanallaringiz:", reply_markup=get_all_chanel_keyboard())
    else:
        await message.answer("Siz botda admin emassiz!!!\n @AzamjonAlijonov")

@router.message(F.text == "Kanal qo'shish")
async def add_chanel(message:Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Hurmatli admin qo'shmoqchi bo'lgan kanalingiz"
                             " username'ini kiriting:", reply_markup=get_cancel_button())
        await state.set_state(AddChanel.add_chanel)
    else:
        await message.answer("Siz botda admin emassiz!!!\n @AzamjonAlijonov")

@router.message(F.text == "Bekor qilish")
async def add_chanel(message:Message, state: FSMContext):
    await state.clear()
    await message.answer("Asosiy menu", reply_markup=get_admin_menu())

@router.message(AddChanel.add_chanel)
async def add_chanel_from_admin(message: Message, state: FSMContext):
    chanel_username = message.text
    if chanel_username.startswith("@") and chanel_username[1:].isalnum():
        await add_chanel_to_db(chanel_username)
        await message.answer("Kanal muvaffaqiyatli qo'shildi!", reply_markup=get_admin_menu())
        await state.clear()
    else:
        await message.answer("Username xato, qayta urining!")