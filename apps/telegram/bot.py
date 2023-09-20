import asyncio
import logging

from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from config import settings as app_settings
from apps.telegram import handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP = Application.builder().token(app_settings.TELEGRAM_BOT_TOKEN).build()


def start():
    APP.add_handler(CommandHandler('start', handlers.start))
    APP.run_polling()


def send_message(chat_id: int, text: str):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(APP.bot.send_message(chat_id=chat_id, text=text))
