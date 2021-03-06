﻿# # -*- coding: utf-8 -*-
# # @Author  : hanzilong
import sys
# sys.path.append("..")
# from conf.config import logs
import logging

# 日志级别等级 CRITICAL > ERROR > WARNING > INFO > DEBUG
class Log():
    def __init__(self,connter):
        # File_log = logs()  # log记录目录
        # 创建一个logger,顶级的根目录getlogger,有两个分支,一个是FileHander,一个是StreamHandler
        logger = logging.getLogger('mian')
        logger.setLevel(logging.INFO)
        # 创建一个handler,将log写入文件
        File_log = "F:\\python_appium框架\\log\\appium.log"
        fh = logging.FileHandler(File_log)
        fh.setLevel(logging.INFO)
        # 再创建一个handler,将log输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 设置输出格式
        log_format = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
        # 把格式添加进来
        formatter = logging.Formatter(log_format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 把handler添加到logger里
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.info(connter)
        # 用pop方法把logger.handlers列表中的handler移除
        # logger.handlers.pop()
        # logger.handlers.pop()
        logger.removeHandler(fh)
        logger.removeHandler(ch)
# if __name__ == '__main__':
#     Log("测试")