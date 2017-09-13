#coding:utf-8
from flaskext.mysql import MySQL
from multiprocessing import Queue
#from ..log import InitLog

mysql = MySQL()
pubQueue = Queue()

"""
	日志系统配置
	1.使用到logging这个模块：
    	import logging
	2.创建一个logger对象：
        logger = logging.getLogger('mylogger')
    3.fileconfig(fname, defaults=None, disable_existing_loggers=True):
    	从指定的fname的配置文件中读取logging配置文件
    	这里的配置文件是log.conf，该文件必须包含[loggers], [handlers]和[formatters]，
    	它们分别代表日志文件中定义的每种类型的实体。
"""

import logging
from logging.config import fileConfig
import os

def InitLog():
    fileConfig(os.path.join
    	       (os.path.dirname(os.path.realpath(__file__)),
    			"log.conf"))
    logger = logging.getLogger("applog")
    return logger

logger = InitLog()

