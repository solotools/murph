import datetime
import os
import random

from common.make_data import data_create


def modify():
    file = open(r'data/ADDRESS.md', "a+", encoding="utf-8")
    file.write(data_create(1) + '\n')
    file.close()


def commit():
    os.system('git commit -a -m "{} add address"'.format(data_create(2)))


def set_sys_time(year, month, day):
    os.system('date %04d/%02d/%02d' % (year, month, day))


def trick_commit(year, month, day):
    set_sys_time(year, month, day)
    modify()
    commit()


def daily_commit(start_date, end_date):
    for i in range((end_date - start_date).days + 1):
        cur_date = start_date + datetime.timedelta(days=i + int('{}'.format(random.randint(1, 5))))
        trick_commit(cur_date.year, cur_date.month, cur_date.day)


if __name__ == '__main__':
    daily_commit(datetime.date(2017, 6, 5), datetime.date(2017, 12, 31))  # 第一个参数为开始日期（小绿点表格左上），第二个结束日期（小绿点表格右下）
    set_sys_time(2020, 6, 30)