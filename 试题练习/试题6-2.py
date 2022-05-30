# _*_coding:utf-8_*_
# @Time : 2022/5/22 15:48
# @Author : 邓必成
# @File :试题练习6-2.PY

a =list(range(10))
print(a)
for i in range(0,10):
    a[i] = int(input(f"输入第{i+1}个整数："))
print(a)

max = a[0]
for i in range(1,10):
    if a[i]>max:
        max =a[i]
print(f"列表 a中的最大值是：{max}")

