#coding:utf-8
import requests

r = requests.get('https://www.baidu.com/')
print r.url
print r.text
