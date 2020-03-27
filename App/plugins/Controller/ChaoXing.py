import os, sqlite3
from nonebot import on_command, CommandSession
from config import *

'''
用户
添加账号
'''


@on_command('cxa', only_to_me=False)
async def cxadd(session: CommandSession):
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    args = session.current_arg_text.strip().split(' ')
    if len(args) != 2:
        await session.send('添加账户 格式:\n/cxa <学习通手机账号> <学习通密码>')
        return
    if len(args) == 2:
        try:
            # 先查询是否存在相同账号
            c.execute('select user from users where user = ?', (args[0],))
            tmp = c.fetchall()
            if len(tmp) != 0:
                await session.send('已存在相同账号!')
            c.execute('select user from users where qq = ?', (session.ctx['user_id'],))
            tmp = c.fetchall()
            if len(tmp) != 0:
                await session.send('该QQ号已绑定账号!')
            if len(tmp) == 0:
                c.execute('insert into users (user, passwd, points, Minterval, qq) values (? , ? , \'100\' ,\'1\' , ?)',(args[0], args[1], session.ctx['user_id']))
                conn.commit()
                await session.send('账号添加成功!')
            conn.close()
        except Exception as e:
            await session.send('账号添加失败!请联系管理员!')
            print(e)


'''
用户
删除账号
'''


@on_command('cxd', only_to_me=False)
async def cxdel(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    try:
        c.execute('select user from users where qq = ? ', (session.ctx['user_id'],))
        queryResult = c.fetchall()
        if len(queryResult) != 0:
            c.execute('delete from users where qq = ?', (session.ctx['user_id'],))
            conn.commit()
            conn.close()
        else:
            await session.send('未找到该QQ绑定的账号!')
            return
        await session.send('账号删除成功!')
    except Exception as e:
        await session.send('账号删除失败!请联系管理员!')
        print(e)


'''
用户
使用卡密
'''
@on_command('cxc', only_to_me=False)
async def cxcdkey(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    if len(args) != 2:
        await session.send('卡密使用格式:\n/cxc <学习通手机账号> <卡密>')
        return
    if len(args) == 2:
        try:
            #查询账号是否存在
            c.execute('select user from users where user = ?', (args[0],))
            tmp = c.fetchall()
            if len(tmp) == 0:
                await session.send('账号不存在!')
                return
            # 查询卡密是否存在
            c.execute('select cdkey from cdkeys where cdkey = ? ', (args[1],))
            tmp = c.fetchall()
            if len(tmp) == 0:
                await session.send('卡密不存在')
                return
            c.execute('UPDATE users set points = points + 1000 where user = ?', [args[0]])
            c.execute('delete from cdkeys where cdkey = ?', [args[1]])
            conn.commit()
            conn.close()
            await session.send('卡密使用成功!积分增加 +1000点!')
        except Exception as e:
            await session.send('卡密使用失败!请联系管理员!')
            print(e)



'''
用户
查询账号状态
'''
@on_command('cxm', only_to_me=False)
async def cxm(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    if len(args) != 2:
        c.execute('select user from users where qq = ?', (session.ctx['user_id'],))
        queryResult = c.fetchall()
        if len(queryResult) == 0:
            await session.send('没有找到绑定的账号!')
            return
        try:
            c.execute('select user, points, Minterval, qq from users where qq = ?', (session.ctx['user_id'],))
            queryResult = c.fetchall()
            if len(queryResult) == 0:
                await session.send('账号或密码错误!')
                return
            await session.send('账号:{0}\n积分:{1}\n监控频率:{2}分钟\n绑定QQ:{3}'.format(queryResult[0][0], queryResult[0][1], queryResult[0][2], queryResult[0][3]))
            conn.close()
        except Exception as e:
            await session.send('查询账号失败!请联系管理员!')
            print(e)
        return
    # if len(args) == 2:


'''
用户
切换监控频率
'''
@on_command('cxb', only_to_me=False)
async def cxb(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    # 初始化数据库
    conn = sqlite3.connect(databasePath)
    c = conn.cursor()
    try:
        c.execute('select user from users where qq = ? ', (session.ctx['user_id'],))
        queryResult = c.fetchall()
        if len(queryResult) != 0:
            if args[0] == '1' or args[0] == '5' or args[0] == '10':
                c.execute('UPDATE users set Minterval = ?  where qq= ?', (args[0],session.ctx['user_id']))
                conn.commit()
                conn.close()
                await session.send('签到监控频率已经切换至 -> {0}分钟'.format(args[0]))
                return
            else:
                await session.send('可用频率 1分钟 | 5分钟 | 10分钟')
        else:
            await session.send('未找到该QQ绑定的账号!')
            return
    except Exception as e:
        await session.send('账号监控频率切换失败!请联系管理员!')
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
        await session.send('发生错误!')
        print(e)
