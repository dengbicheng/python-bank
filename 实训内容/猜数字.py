# _*_coding:utf-8_*_
# @Time : 2022/3/12 22:59
# @Author : 邓必成
# @File :实训案例4.PY

#提示版本
"""
import random  #导入随机模块

a = random.randint(1,100)  #随机生成1-100的整数

b = 1  #运行的次数

c = int(input("请输入你想猜的数：")) #用户输入一个数

while a != c:  #判断a和c，当a不等于c则循环运行，等于则结束循环

    if b == 5:  #判断b，当b等于5时则停止运行
        print("你猜了五次都没中你有什么用")
        print("正确的数为：%d" %a)
        break #跳出循环

    if a > c:
        b += 1
        print("傻逼没猜中数值小了")
        c = int(input("请输入你想猜的数："))

    elif a < c:
        b +=1
        print("傻逼你猜中的数值大了")
        c = int(input("请输入你想猜的数："))

else:
    print("恭喜你，你猜了%d次猜中了"%b)
"""


#无提示版本
"""
import random
a = random.randint(1,100)
b = 1
c = int(input("输入一个数："))
while a != c:
   if b == 5:
       print("超过五次很遗憾，正确数为：%d"%a)
       exit(b)
   if a != c:
       b += 1
       c = int(input("输入一个数："))
else:
    print("你猜了%d次猜对了"%b)
"""

# 剩余提示版

import random
a = random.randint(1,101)        #随机生成一个1-100的数

b = 5                            #机会次数

d = 1                            #计数用的

c = int(input("请输入一个数你有%d次机会："%b))      

while a != c:                   #当随机数不等于你输入的数时则循环运行下面的语句，否则终止循环
    
    if b == 1:                  #当次数为1时结束循环
        
        print("你给你机会你不中用啊，正确数为：%d"%a)
        break

    if a > c:                   #输入的数值小于随机数时给你个提示并且次数减一
        
        b -= 1
        print("傻逼没猜中数值小了")
        c = int(input("请输入一个数你还有%d次机会："%b))
        d += 1                  #计数加一

    elif a < c:
        
        b -= 1
        print("傻逼你猜中的数值大了")
        c = int(input("请输入一个数你还有%d次机会：" % b))
        d += 1

else:
    print("恭喜你猜了%d次猜对了"%d)
