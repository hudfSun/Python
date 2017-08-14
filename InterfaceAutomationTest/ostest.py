#coding:utf-8

f = u'name:\u7cfb\u7edf\u68c0\u6d4b'
s = f[5:len(f)]

print f 
print f.encode('utf-8')
print s
s1=unicode('哈', 'utf-8') 
print s1