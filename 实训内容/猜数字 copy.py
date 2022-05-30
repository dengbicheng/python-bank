# _*_coding:utf-8_*_

""" 猜数字 """

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
