from .start import router as start_router
from .help import router as help_router

# Здесь регистрируем все обработчики для удобного импорта в bot.py
__all__ = ["start_router", "help_router"]
