# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 10:37
# @Author  : 李佳玮
# @Email   : lijiawei@symbio.com
# @File    : debug.py
# @Software: PyCharm
import datetime
import random

a = datetime.date(2017, 6, 16) + datetime.timedelta(days=int('{}'.format(random.randint(1, 5))))
print(a)