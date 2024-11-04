import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import start, help
import logging


# Создаем экземпляр бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Регистрируем маршруты из обработчиков
dp.include_router(start.router)
dp.include_router(help.router)


async def main():
    logging.info("Бот запускается...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
