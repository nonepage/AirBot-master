from nonebot import on_command, CommandSession
import requests
import socket
import asyncio
from concurrent.futures import ThreadPoolExecutor

@on_command('ip', only_to_me=False)
async def ipinfo(session: CommandSession):
    async def get_ipinfo(ipaddr):
        loop = asyncio.get_event_loop()
        addr = socket.gethostbyname(ipaddr)
        with ThreadPoolExecutor(max_workers=5) as pool:
            task = await loop.run_in_executor(pool, requests.get, 'http://ip-api.com/json/' + addr)
            task = task.json()
            country = task['country']
            area = task['isp']
            report = 'IP地址：' + addr + '\n' + 'Country：' + country + '\n' + 'ISP：' + area
            await session.send(report)

    ipaddress = session.get('ipaddress', prompt='请发送需要查询的IP地址.')
    asyncio.create_task(get_ipinfo(ipaddress))

@ipinfo.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['ipaddress'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('查询地址不能为空，请重新输入.')
    session.state[session.current_key] = stripped_arg
