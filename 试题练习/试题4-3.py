# _*_coding:utf-8_*_
# @Time : 2022/5/23 16:17
# @Author : 邓必成
# @File :试题练习4-3.PY


def jiecheng(n):  #n的阶乘
    if n == 1:
        a = 1
    else:
        a = n*jiecheng(n-1)
    return a
n = int(input("请输入一个整数："))
sum = 0
for i in range(1,n+1):
    sum += 1/jiecheng(i)
#保留4位小数
print(f"{sum:.4f}")


#方法二
'''
sum = 0
for i in range(1,5+1):
    fac = 1
    for j in range(1,i+1):
        fac *= j
    sum += 1/fac
print(f"{sum:.4f}")
'''
    

