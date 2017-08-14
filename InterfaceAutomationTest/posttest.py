#coding:utf-8

import requests
import json

url = 'https://passport.cnblogs.com/user/signin'
par = {"input1":"Bz7bQzdqOTpVPPmKtUVva3gxVt9HPAmHeWcScvyig9CxKEphnlg2fHGOTM4gXkx3zDnBV2JjyG3HebJuJUtEyEoAd6c3TXTPBVvkncThZUERlTXUBMo85LmGAI+y3u6eDTxdDtY085VeXjwVSvsxKOhQ9m+GZGgpbIjGMELisME=",
       "input2":"I41M+GxPhCZZ9N2kHePtoL6R3DtSwav9oFMVauYuNOyOugeSiFYKjJTamnsMMZn3SQ8ZqOvI30fhYfIrrU2Q6FN703h4tjK76j5B3OZU5D83fKbnmaEg43zS9XIPpt2HgAOinqs4Wmqq4M5bMYJlH8VmLDfZ6maYuWGoyCeOgaI=",
       "remember":False}
heard = {
    'User-Agent':'Mozilla/5.0(Windows NT6.1;WOW64;RV:54.0)Gecko/20 100 10 1 Firefox/54.0',
    'Accept':'application/json,text/javascript',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5;q=0.3',
    'Accept-Encoding':'gzip,deflate,br',
    'Content-Type':'application/json;charest=utf-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie':'ga=GA1.2.1928922384.1498022132; _gid=GA1.2.2011048131.1498443278; _gat=1; SERVERID=9b2e527de1fc6430919cfb3051ec3e6c|1498443285|1498443281',
    'Connection':'keep-alive'
}
s = requests.session()
# print s
r = s.post(url,json=par,headers=heard,verify=False)

# print r.status_code
# print r.text
t=  r.json()
print t
print s.cookies
url2 = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
body = {'__VIEWSTATE':'',
     'Editor$Edit$txbTitle':	u'1231313123123这是一个草稿52',
     'Editor$Edit$EditorBody':	u'<p>42412414141哈哈哈哈</p>',
     'Editor$Edit$Advanced$ckbPublished':'on',
     'Editor$Edit$Advanced$chkDisplayHomePage':'on',
     'Editor$Edit$Advanced$chkComments':'on',
     'Editor$Edit$Advanced$chkMainSyndication':'on',
     'Editor$Edit$Advanced$txbEntryName':''	,
     'Editor$Edit$Advanced$txbExcerpt':'',
     'Editor$Edit$Advanced$txbTag':'',
     'Editor$Edit$Advanced$tbEnryPassword':'',
     'Editor$Edit$lkbDraft':'存为草稿'
 }
 
r2 = s.post(url2,data=body,verify=False)
# print r2.content