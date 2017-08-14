# coding:utf-8
import requests
#  先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"          }  # get方法其它加个ser-Agent就可以了
r = requests.get(url, headers=headers,verify=False)
print r.cookies  # 添加前的cookies# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()
c.set('.CNBlogsCookie', 'xxx')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies','xxx')  # 填上面抓包内容
r.cookies.update(c)
print r.cookies  # 添加后的cookies
