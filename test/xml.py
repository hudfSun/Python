#-*- coding: UTF-8 -*-
import os
import sys
from JavaFilter import *

import linecache
reload(sys)
sys.setdefaultencoding('utf8')
# # 遍历指定目录，显示目录下的所有文件名
# def eachFile(filepath):
#     pathDir =  os.listdir(filepath)
#     for allDir in pathDir:
#         child = os.path.join('%s%s' % (filepath, allDir))
#         print child.decode('gbk') # .decode('gbk')是解决中文显示乱码问题

def getFiles(path, rule=".java"):
    all = []
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            filename = os.path.join(fpathe,f)
            if filename.endswith(rule):
                all.append(filename)
    return all


if __name__ == '__main__':
    # file = "/Users/zhangli/Documents/testFile"
    #file="D:/"
    totalAll = 0
    filePathList = getFiles("D:\imobilegw-master")
    #eachFile(file)
    for fileName in filePathList:
        totalAll = totalAll + JavaFilter.readFile(fileName)
    print "找到Hardcode", totalAll,"处，请您检查。"
