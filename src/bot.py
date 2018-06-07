import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

from get_mirror import get_current_mirror


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=f"{get_current_mirror()}")
    print('Sending mirror')


def polling():
    updater = Updater(token=os.environ.get('TOKEN'))
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
