#coding:utf-8
import requests

url_path = 'http://zzk.cnblogs.com/s/blogpost'
par = {'kewwords':'python'}
headers = {'Connection': 'keep-alive'}
r = requests.get(url=url_path,params=par,headers=headers)
# print r.text
# print r.content
print  r.url
print r.encoding
print r.cookies
print r.reason
print r.headers