import os

from nonebot.default_config import *

SUPERUSERS = {1038888008}
API_ROOT = 'http://127.0.0.1:5700'
''''
超星学习通
'''
databasePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database', 'data.db')
API = 'http://101.89.182.58:9090/sign/?username={0}&password={1}'
headers = {
    'Accept': 'application/json',
}
''''
Lang
'''
ChaoXingDelAccountMissingparameters = '删除账户 格式:\n/cxdel <账号> <密码>'
ChaoXingDelAccountOK = '账号删除成功!'
ChaoXingDelAccountError = '账号删除失败!请联系管理员!'

ChaoXingAddAccountMissingparameters = '添加账户 格式:\n/cxadd <账号> <密码>'
ChaoXingAddAccountOK = '账号添加成功!'
ChaoXingAddAccountError = '账号添加失败!请联系管理员!'

ChaoXingShowAllAccountError = '发生错误!'
