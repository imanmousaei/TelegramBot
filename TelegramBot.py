import telegram
import config 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class TelegramBot:
    def __init__(self, bot_token=config.bot_token):
        self.bot_token = bot_token
        self.bot = telegram.Bot(token=self.bot_token)
        self.app = ApplicationBuilder().token(self.bot_token).build()

    def send_msg(self, msg):
        for chat_id in config.chat_ids:
            self.bot.sendMessage(chat_id=chat_id, text=msg)

    def send_admins(self, msg):
        for chat_id in config.admin_chat_ids:
            self.bot.sendMessage(chat_id=chat_id, text=msg)

    def get_updates(self):        
        updates = self.bot.get_updates()
        return updates

    def add_handler_for_command(self, command, handler):
        self.bot.add_handler(CommandHandler(command, handler))

    def run(self):
        self.app.run_polling()
