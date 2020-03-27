from nonebot import on_command, CommandSession
import requests
import socket


@on_command('help', only_to_me=False)
async def ipinfo(session: CommandSession):
    await session.send('超星学习通自动签到机器人 v1.0.2\n'                     
                       '指令列表:\n'
                       '/cxa 绑定账号\n'
                       '/cxd 删除当前QQ绑定的学习通账号\n'
                       '/cxm 查看当前QQ绑定的信息\n'
                       '/cxc 使用卡密充值积分\n'
                       '/cxb 切换签到监控频率'
                       )