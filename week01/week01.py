import logging
from pathlib import Path
import os
import time


def week01_log():
    time_now = time.strftime("%Y-%m-%d" ,time.localtime())
    p = Path()
    path = str(p.resolve())+ f"/var/log/python-{time_now}/"

    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)
    logging.basicConfig(filename='python.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [Line: %(lineno)d] %(message)s') 
                        )
    logging.debug('显示为函数被调用时间')


if __name__ == '__main__':
    week01_log()