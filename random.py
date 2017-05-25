# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
#生成随机整数并输出至本地文件
import random2
for i in range(0,2000):
    print('test time:' + str(i) + '=============>')
    c = random2.randint(13512345678, 13612345678)#取随机手机号码
    f = open('f:/1/test.txt','a')#用a不会被复写，用w会被复写
    print >> f,c
else:
    f.close()