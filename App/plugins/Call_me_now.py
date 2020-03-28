import datetime
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.cron import CronTrigger
from nonebot import on_command, scheduler, CommandSession
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import sqlite3
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from config import database_call
from apscheduler.schedulers.background import BackgroundScheduler


@on_command('clock', aliases=('闹钟', '定个闹钟'), only_to_me=False)
async def main_clock(session: CommandSession):
    time = session.get('time', prompt=r'请问您要定一个几点的闹钟?')

    # 初始化scheduler

    # scheduler.add_jobstore('defualt', url='sqlite:///' + database_call)
    # call_jobstore = {
    #     'callme': SQLAlchemyJobStore(url='sqlite:///' + database_call)
    # }

    # 制作一个“5分钟后”触发器
    delta = datetime.timedelta(minutes=float(time))
    trigger = DateTrigger(
        run_date=datetime.datetime.now() + delta
    )

    # 添加任务
    scheduler.add_job(
        func=session.send,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        args=('您定的闹钟时间到了',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        misfire_grace_time=60,
        # id='1',
    )

    await session.send('已经为您订好了一个' + time + '分钟的闹钟')


@main_clock.args_parser
async def _(session: CommandSession):
    reust = session.current_arg_text.strip()

    if session.is_first_run:
        if reust and int(reust) <= 1440:
            session.state['time'] = reust
            return

    if not reust:
        session.pause('请输入时间,例如1(1分钟)')

    if reust and int(reust) > 1440:
        session.pause('请重新输入小于1440的数!')
    session.state['time'] = reust


@on_command('schedule', aliases=('日程', '定个日程'), only_to_me=False)
async def main_clock(session: CommandSession):
    time = session.get('time', prompt=r'请问您要定一个几点的日程?列如:18.18(6点18分)')
    # 制作一个“5分钟后”触发器
    time = time.split('.', 1)
    if len(time) < 2:
        time.append('00')
    trigger = CronTrigger(
        hour=time[0],
        minute=time[1]
    )

    # 添加任务
    scheduler.add_job(
        func=session.send,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        args=('您定的日程时间到了',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        misfire_grace_time=60, )
    await session.send('已经为您订好了一个每天' + time[0] + ':' + time[1] + '的日程')


@main_clock.args_parser
async def _(session: CommandSession):
    reust = session.current_arg_text.strip()
    if session.is_first_run:
        if reust:
            session.state['time'] = reust
            return

    if not reust:
        session.pause('请输入时间列如:22.11(晚上十点11分)')

    session.state['time'] = reust
