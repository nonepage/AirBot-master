from os import path
import config
import nonebot
import sqlite3
import os
from App.Tools.ChaoXingCdkeyGR import *
if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'App', 'plugins'),
        'App.plugins',
    )
    if not os.path.exists(config.databasePath):
        conn = sqlite3.connect(config.databasePath)
        try:
            c = conn.cursor()
            c.execute(
                'create table users (user varchar(12) , passwd varchar(64) , points int(64) , Minterval int '
                '(64) , qq varchar (64))')
            c.execute(
                'create table cdkeys (cdkey varchar(128))')
            conn.commit()
            conn.close()
        except Exception as e:
            print("create database failed" + str(e))
    nonebot.run(host='127.0.0.1', port=8080)