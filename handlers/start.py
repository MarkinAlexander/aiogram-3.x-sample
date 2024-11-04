from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command  # импортируем фильтр Command

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я бот на aiogram 3.x. Чем могу помочь?")
