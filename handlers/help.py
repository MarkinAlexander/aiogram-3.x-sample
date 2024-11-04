from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command  # импортируем фильтр Command

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Список доступных команд:\n/start - Начало работы\n/help - Помощь")
