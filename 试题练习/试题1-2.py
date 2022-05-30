#从键盘输入一个整数 N，打印出的三角形和到三角形


a = int(input("请输入行数值（2<=a<=20）："))

#方法一
"""
b = 1
c = 10
if 2 <= a <= 20:
    while b <= a:
        print(" "*(c-b)+"*"*(2*b-1))
        
        b += 1
    while b >= 1:
        print(" "*(c-b)+"*"*(2*b-1))
        
        b -= 1
else:
    print("你输入的数值有误")
"""

#方法二
if 2 <= a <= 20:
    for i in range(1,a+1):
        print(" "*(a-i)+"*"*(2*i-1))
    for i in range(a-1,0,-1):
        print(" "*(a-i)+"*"*(2*i-1))
else:
    print("你输入的数值有误")






