# _*_coding:utf-8_*_
# @Time : 2022/3/20 9:42
# @Author : 邓必成
# @File :实训案例九.PY

"""
#方法一
print("<------xyz=816,xyz分别代表什么数------>")
for x in range(0,10):
    for y in range(0, 10):
        for z in range(0, 10):
            if x*100+y*10+z+y*100+z*10+z==816:
                print("\nx代表：%d""\ny代表：%d""\nz代表：%d"%(x,y,z))
                break
"""

#方法二
for a in range(100,816-100):
    x = a//100
    y = a%100//10
    z =a%10

    b = 816-a
    x2 = b // 100
    y2 = b // 10 % 10
    z2 =b % 10
    if y ==x2 and z==y2 and z==z2:
        print(f"x:{x},y:{y},z:{z},{a}+{b}=816")
        break
