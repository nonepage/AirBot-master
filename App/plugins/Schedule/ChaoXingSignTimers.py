import sqlite3
import requests as r
import nonebot
from config import *

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
        for x in accountList:
            if "暂无" not in r.post(API.format(x[0], x[1]), headers=headers).text:
                c.execute('UPDATE users set points = points - 40 where user = ?', [x[0]])
                conn.commit()
                qq = c.execute('select qq from users where user = ?', [x[0]])
                for i in qq:
                    await bot.send_private_msg(user_id=i[0], message='签到成功 积分扣除 -40点')
    except nonebot.CQHttpError:
        print('消息回调发生失败可能 没有权限、对方不是好友、无 API 连接等')
    except Exception as e:
        print(e)


'''
5分钟监控
'''

'''
10分钟监控
'''
