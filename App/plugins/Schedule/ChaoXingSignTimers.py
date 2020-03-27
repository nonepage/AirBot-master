import sqlite3 , threading
import requests as r
import nonebot
import asyncio
from config import *
from App.Tools.ChaoXingSign import AutoSign
'''
1分钟监控
'''

@nonebot.scheduler.scheduled_job('interval', minutes=1)
async def oneMinutes():
    bot = nonebot.get_bot()
    try:
        conn = sqlite3.connect(databasePath)
        c = conn.cursor()
        accountList = c.execute('select user ,passwd from users where Minterval = 1')
        for x in accountList.fetchall():
            points = c.execute('select points from users where user = ? ', [x[0]])
            if points.fetchall()[0][0] < 40:
                continue
            if "签到成功" in r.post(API.format(x[0], x[1]), headers=headers).text:
                #print(r.post(API.format(x[0], x[1]), headers=headers).text)
                c.execute('UPDATE users set points = points - 40 where user = ?', [x[0]])
                conn.commit()
                #qq = c.execute('select qq from users where user = ?', [x[0]])
                #queryResult = qq.fetchall()
                # await bot.send_private_msg(user_id=queryResult[0][0], message='签到成功 积分扣除 -40点')
                #await bot.send_group_msg(group_id=782621442, message='{0}签到成功 积分扣除 -40点'.format(x[0]))
    except nonebot.CQHttpError:
        print('消息回调发生失败可能 没有权限、对方不是好友、无 API 连接等')
    except Exception as e:
        print(e)
'''
5分钟监控
'''
@nonebot.scheduler.scheduled_job('interval', minutes=5)
async def WuMinutes():
    bot = nonebot.get_bot()
    try:
        conn = sqlite3.connect(databasePath)
        c = conn.cursor()
        accountList = c.execute('select user ,passwd from users where Minterval = 5')
        for x in accountList.fetchall():
            points = c.execute('select points from users where user = ? ', [x[0]])
            if points.fetchall()[0][0] < 25:
                continue
            if "签到成功" in r.post(API.format(x[0], x[1]), headers=headers).text:
                c.execute('UPDATE users set points = points - 25 where user = ?', [x[0]])
                conn.commit()
                #qq = c.execute('select qq from users where user = ?', [x[0]])
                #queryResult = qq.fetchall()
                #await bot.send_private_msg(user_id=queryResult[0][0], message='签到成功 积分扣除 -25点')
    except nonebot.CQHttpError:
        print('消息回调发生失败可能 没有权限、对方不是好友、无 API 连接等')
    except Exception as e:
        print(e)
'''
10分钟监控  有问题 懒得修了...
'''
@nonebot.scheduler.scheduled_job('interval', minutes=10)
async def tenMinutes():
    bot = nonebot.get_bot()
    try:
        conn = sqlite3.connect(databasePath)
        c = conn.cursor()
        accountList = c.execute('select user ,passwd from users where Minterval = 10')
        for x in accountList.fetchall():
            points = c.execute('select points from users where user = ? ', [x[0]])
            if points.fetchall()[0][0] < 10:
                continue
            if "签到成功" in r.post(API.format(x[0], x[1]), headers=headers).text:
                c.execute('UPDATE users set points = points - 10 where user = ?', [x[0]])
                conn.commit()
                #qq = c.execute('select qq from users where user = ?', [x[0]])
                #queryResult = qq.fetchall()
                #await bot.send_private_msg(user_id=queryResult[0][0], message='签到成功 积分扣除 -10点')
    except nonebot.CQHttpError:
        print('消息回调发生失败可能 没有权限、对方不是好友、无 API 连接等')
    except Exception as e:
        print(e)