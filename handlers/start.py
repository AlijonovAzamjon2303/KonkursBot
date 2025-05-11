from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import ADMINS
from keyboards.reply import get_admin_menu

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}")

    if message.from_user.id in ADMINS:
        await message.answer("Hurmatli admin botga xush kelibsiz!", reply_markup=get_admin_menu())