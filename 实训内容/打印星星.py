# _*_coding:utf-8_*_
# @Time : 2022/3/13 18:49
# @Author : 邓必成
# @File :实训案例六.PY
a = int(input("请输入行数值（2<=a<=20）："))
b = 1
c = 65
if 2 <= a <= 20:
    while b <= a:
        print(" "*(c-b)+"*"*(2*b-1))
        print()
        b += 1
    while b >= 1:
        print(" "*(c-b)+"*"*(2*b-1))
        print()
        b -= 1
else:
    print("你输入的数值有误")