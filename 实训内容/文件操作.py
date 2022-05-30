# _*_coding:utf-8_*_

import random

with open('hello.txt','w+',encoding='utf-8') as f:      #打开一个文件编码方式为"utf-8"
    
    f.write('hello world')                #写入一个内容                         

#写入200个随机数满足20个就换行
    for i in range(0,200):                      #循环200次
        if i % 20 == 0:                         #当i的余为0时则换行
            f.write("\n")
        f.write(str(random.randint(0,100)))     #写入一个1-100的随机数（注意这个数要为字符型）
        f.write(" ")
f.close()                                     #关闭文件




  


    
