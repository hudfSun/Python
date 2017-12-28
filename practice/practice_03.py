#coding:utf-8
#题目：一个整数，它加上100后是一个完全平方数，
# 再加上168又是一个完全平方数，请问该数是多少？
import math

for m in range(1,168):
    for n in range(1,m):
        if ((m+n)*(m-n))==168:
            x = n**2-100
            if x >2 and x< 168:
                print("这个数是%s"%x)