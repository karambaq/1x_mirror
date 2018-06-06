import requests

def get_current_mirror():
    try:
        cur_mirror = requests.get('http://1xstavka.ru').url.split('?')[0]
    except Exception as e:
        return "1xbet doesn't work for now"

    return cur_mirror
