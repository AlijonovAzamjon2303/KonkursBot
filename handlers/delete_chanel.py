from aiogram import Router, F
from aiogram.types import CallbackQuery

from database.admin import get_chanel_by_id, delete_chanel_by_id
from keyboards.inline import get_confir_to_delete, get_all_chanel_keyboard

router = Router()

@router.callback_query(F.data.startswith("chanel_"))
async def delete_chanel(callback: CallbackQuery):
    id = int(callback.data.split("_")[1])
    chanel = get_chanel_by_id(id)
    await callback.message.edit_text(f"Siz rostdan ham {chanel[1]} ni o'chirmoqchimisiz", reply_markup=get_confir_to_delete(id))

@router.callback_query(F.data.startswith("confirm_"))
async def delete_chanel_from_db(callback:CallbackQuery):
    id = int(callback.data.split("_")[1])
    chanel = get_chanel_by_id(id)
    delete_chanel_by_id(id)
    await callback.message.edit_text(f"{chanel[1]} kanal muvaffaqiyatli o'chirildi."
                                     f"\nYana o'chirishni istasangiz ustiga bosing va tasdiqlang", reply_markup=get_all_chanel_keyboard())

@router.callback_query(F.data.startswith("cancel_"))
async def delete_chanel_from_db(callback:CallbackQuery):
    await callback.message.edit_text("Biror kanalni o'chirish uchun ustiga bosing"
                                     " va tasdiqlang", reply_markup=get_all_chanel_keyboard())