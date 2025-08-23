import logging

# Logger yaratamiz
logger = logging.getLogger("bot_logger")
logger.setLevel(logging.INFO)

# Format (millisekundgacha aniqlikda vaqt)
formatter = logging.Formatter(
    "%(asctime)s.%(msecs)03d - LEVEL:%(levelname)s - USER_ID:%(user_id)s - NAME:%(full_name)s - USERNAME:%(username)s - MESSAGE:%(message)s",
    "%Y-%m-%d %H:%M:%S"
)

# Konsolga chiqarish
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Faylga yozish
file_handler = logging.FileHandler("bot_logs.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def log_action(user, action: str):
    """Foydalanuvchi qilgan amallarni log qiladi"""
    extra = {
        "user_id": user.id,
        "full_name": user.full_name,
        "username": f"@{user.username}" if user.username else "None"
    }
    logger.info(action, extra=extra)


def log_system(message: str, level="info"):
    """Bot tizimi loglari (start, error, stop va boshqalar)"""
    extra = {
        "user_id": "-",
        "full_name": "-",
        "username": "-"
    }
    if level == "error":
        logger.error(message, extra=extra)
    elif level == "warning":
        logger.warning(message, extra=extra)
    else:
        logger.info(message, extra=extra)
