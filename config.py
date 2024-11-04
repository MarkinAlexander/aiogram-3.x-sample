import logging
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле")
