import os, sqlite3
from nonebot import on_command, CommandSession
from config import *

'''
用户
添加账号
'''


@on_command('cxadd', only_to_me=False)
async def cxadd(session: CommandSession):
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    args = session.current_arg_text.strip().split(' ')
    if len(args) != 2:
        await session.send(ChaoXingAddAccountMissingparameters)
        return
    if len(args) == 2:
        try:
            c.execute('select user from users where user = ?', (args[0],))
            tmp = c.fetchall()

            # print(tmp[0][0],type(tmp))
            if len(tmp) == 0:
                c.execute('insert into users (user, passwd, points, Minterval, qq) values (? , ? , \'100\' ,\'1\' , ?)',(args[0], args[1], session.ctx['user_id']))
                conn.commit()
                await session.send(ChaoXingAddAccountOK)
            else:
                await session.send('已存在相同账号!')
            conn.close()
        except Exception as e:
            await session.send(ChaoXingAddAccountError)
            print(e)


'''
用户
删除账号
'''


@on_command('cxdel', only_to_me=False)
async def cxdel(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    if len(args) != 2:
        await session.send(ChaoXingDelAccountMissingparameters)
        return
    if len(args) == 2:
        try:
            c.execute('delete from users where user = ? and passwd = ?', (args[0], args[1]))
            conn.commit()
            conn.close()
            await session.send(ChaoXingDelAccountOK)
        except Exception as e:
            await session.send(ChaoXingDelAccountError)
            print(e)


'''
管理员 
查询所有账号
'''


@on_command('cxuserall', only_to_me=False)
async def cxuserall(session: CommandSession, ):
    args = session.current_arg_text.strip().split(' ')
    if not session.ctx['user_id'] in SUPERUSERS:
        await session.finish('抱歉!你没有权限这么做!')
        return
    result = ''
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    try:
        sqldata = c.execute('select user ,passwd from users')
        for x in sqldata:
            result += str(x) + '\n'
        await session.send(result)
    except Exception as e:
        await session.send(ChaoXingShowAllAccountError)
        print(e)
