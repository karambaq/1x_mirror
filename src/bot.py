import os

from telegram.ext import Updater
from telegram.ext import CommandHandler
from requests_html import HTMLSession


def get_current_mirror():
    """
    Returns current available mirror of the 1xbet.com, 
    first try to redirects, if fails, try to use google
    """
    REQUESTS_COUNT += 1
    print(REQUESTS_COUNT)
    session = HTMLSession()
    url = 'http://1xstavka.ru'
    try:
        return session.get('http://1xstavka.ru').url.split('?')[0]
    except Exception as e:
        url = 'https://www.google.ru/search?&q=1xbet.com'
        try:
            r = session.get(url)
        except Exception as e:
            return "Second try, doesn't work"

        return r.html.search('⇒ {} ⇒')[0]


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=f"{get_current_mirror()}")
    print('Sending mirror')


def polling():
    global REQUESTS_COUNT
    REQUESTS_COUNT = 0
    updater = Updater(token=os.environ.get('TOKEN'))
    start_handler = CommandHandler('start', start) 
    updater.dispatcher.add_handler(start_handler) 
    updater.start_polling() 
