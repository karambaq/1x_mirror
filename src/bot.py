import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

from get_mirror import get_current_mirror


def start(bot, update):
    REQUESTS_COUNT += 1
    print(REQUESTS_COUNT)
    bot.sendMessage(chat_id=update.message.chat_id, text=f"{get_current_mirror()}")


def polling():
    REQUESTS_COUNT = 0
    updater = Updater(token='607298602:AAHmHXlRkNJ3rT2dPiij3Ah2hAy0gnu7M6w')
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
