# _*_coding:utf-8_*_
# @Time : 2022/5/23 15:28
# @Author : 邓必成
# @File :试题5-2.PY
print("-----函数的方法---------")
def jiecheng(n):  #n的阶乘
    if n == 1:
        a = 1
    else:
        a = n*jiecheng(n-1)
    return a

mun = 0
for i in range(1,11):
    mun += jiecheng(i)  #计算1-10的阶乘
print(f"1-10相加的阶乘是：{mun}")


print("\n","-----双重循环的方法-----")
sum = 0
for i in range(1,11):
    n = 1
    for j in range(1,i+1):
        n = j * n
    sum =sum + n
print(f"1-10相加的阶乘是：{sum}")