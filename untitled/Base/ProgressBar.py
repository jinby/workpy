
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-21 下午3:44
# @Author  : LK
# @File    : 进度条.py
# @Software: PyCharm
import sys
import math


class ProgressBar(object):
    def __init__(self, file_name, total):
        self._total = total
        self._file_name = file_name

    def move(self, cur):
        percent = '{:.2%}'.format(cur / self._total)
        sys.stdout.write('\r')
        sys.stdout.write("[%-50s] %s %s" % ('=' * int(math.floor(cur * 50 / self._total)),  percent, self._file_name))
        sys.stdout.flush()

    def end(self):
        sys.stdout.write('\n')

if __name__ == '__main__':
    import time

    bar1 = ProgressBar("123", 100)
    for i in range(100):
        bar1.move(i+1)
        time.sleep(0.2)
    bar1.end()

    bar1 = ProgressBar("222", 100)
    for i in range(100):
        bar1.move(i+1)
        time.sleep(0.2)
    bar1.end()

