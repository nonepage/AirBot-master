from nonebot import on_command, CommandSession
import requests
import socket


@on_command('help', only_to_me=False)
async def ipinfo(session: CommandSession):
    await session.send('幽忆云 bot v1.0.2\n'
                       'by 单字汪\n'
                       '其余贡献者:\n'
                       'nonepage\n'
                       '\n\n'
                        
                       
                       '指令列表:\n'
                       '/ip 查询IP消息\n'
                       '/gfwtcp 被墙检测\n'
                       '/gfwdns 查询域名DNS信息\n'
                       '----------------------------\n'
                       '***欢迎其他开发者加入***\n开源项目地址:https://github.com/result-bit/AirBot'
                       )