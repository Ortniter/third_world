import logging

from telegram import Update
from telegram.ext import ContextTypes

from config.db import SessionLocal
from apps.users.models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with SessionLocal() as db:
        User.create_or_update(
            db=db,
            username=update.effective_chat.username,
            telegram_id=update.effective_chat.id,
            first_name=update.effective_chat.first_name,
            last_name=update.effective_chat.last_name
        )

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hi there! I\'ll show you what that folders hide.'
    )
