import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

from get_mirror import get_current_mirror


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=f"{get_current_mirror()}")
    REQUESTS_COUNT += 1
    print('Sending mirror')
    print(REQUESTS_COUNT)


def polling():
    global REQUESTS_COUNT
    REQUESTS_COUNT = 0
    updater = Updater(token=os.environ.get('TOKEN'))
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
