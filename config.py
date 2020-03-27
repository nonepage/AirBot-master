import os

from nonebot.default_config import *

SUPERUSERS = {1038888008}
API_ROOT = 'http://127.0.0.1:5700'
''''
超星学习通
'''
databasePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'data.db')
activeid_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'activeid.txt')
cookies_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'cookies.json')
API = 'http://49.234.226.191/sign/?username={0}&password={1}'
headers = {
    'Accept': 'application/json',
}

