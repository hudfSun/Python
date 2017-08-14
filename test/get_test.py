#coding:utf-8
import requests


r = requests.get('http://www.cnblogs.com/yoyoketang')
print r.text
print r.content