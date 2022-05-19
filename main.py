from telegram import Update
from telegram.ext import ContextTypes

from TelegramBot import TelegramBot


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

bot = TelegramBot()
bot.add_handler_for_command('hello', hello)
bot.run()
