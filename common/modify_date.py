import os

from green import modify


def set_sys_time(year, month, day):
    os.system('date %04d/%02d/%02d' % (year, month, day))

set_sys_time(2019, 6, 13)
modify()