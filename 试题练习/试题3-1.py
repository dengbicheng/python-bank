# _*_coding:utf-8_*_
# @Time : 2022/5/23 16:17
# @Author : 邓必成
# @File :试题3-1.PY

#输入三个整数 x、y、z把这三个数由小到大输出
x,y,z = map(int,input("输入三个整数用空格隔开：").split(" "))

if x > y:       #如果x大于y，则交换x和y的值
    x,y = y,x
if x > z:       #如果x大于z，则交换x和z的值
    x,z = z,x
if y > z:       #如果y大于z，则交换y和z的值
    y,z = z,y

print(x,y,z)







