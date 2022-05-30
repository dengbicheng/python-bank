# _*_coding:utf-8_*_
# @Time : 2022/5/22 16:23
# @Author : 邓必成
# @File :试题练习6-3.PY
n = input("输入一个整数：")
def fun(n):
    a = 1
    for i in range(0,len(n)):
        a *= int(n[i])
    return a

a = fun(n)
print(f"正整数{n}的各个数位上的数字之积为：{a}")
