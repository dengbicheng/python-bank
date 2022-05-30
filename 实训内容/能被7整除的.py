# _*_coding:utf-8_*_
# @Time : 2022/3/13 14:20
# @Author : 邓必成
# @File :实训案例五.PY
n = int(input("请输入 限值n（2<=n<=1000）："))
t = 1
count = 0
s = 0
if 2 <=n <=1000:
    while t <= n:
        if t%7 == 0:
            count += 1
            s += t
        t += 1
    print("1-%d 之间能被 7 整除的个数：%d" % (n,count))
    print("1-%d 之间能被 7 整除的和值：%d" % (n,s))
else:
    print("输入有误")



