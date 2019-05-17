import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

token = "REMOVED_TELEGRAM_TOKEN"
bot = telegram.Bot(token = token)
def get_message(bot, update) :
    update.message.reply_text(update.message.text)
updater = Updater(token)
messagehandler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(messagehandler)

updater.start_polling(timeout=10, clean=True)
updater.idle()
