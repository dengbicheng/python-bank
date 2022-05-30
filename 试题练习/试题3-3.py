# _*_coding:utf-8_*_
# @Time : 2022/5/23 18:34
# @Author : 邓必成
# @File :试题3-3.PY

#输入整数 a 和 n，输出结果 s，其中s=a+aa+aaa+aaaa+aa...a

#方法一
'''
a = int(input("请输入一个数字："))
n = int(input("请输入一个数字，决定相加个数"))
if not 2 <= a <= 9:
    print("你输入的数值有误")
else:
    sum = 0
    c = a   #这里等于a是为了让每一次循环的时候，c的值都为a

    #for语句
    for i in range(1,n+1):
        sum = a + sum
        a = a + c * (10**i)
        print(sum)
'''

'''
    #while语句
    sum = 0
    i = 1
    while i <= n:
        sum = a + sum
        a = a + c * (10**i)
        i += 1
    print(sum)
'''
#方法二
'''
a = int(input("请输入数字："))
b = int(input("请输入相加个数："))
if not 2 <= a <= 9:
    print("你输入的数值有误")
else:
    aa,sum = 0,0    #初始值
    for i in range(1,b+1):
        aa += a * 10 ** (i-1)     
        sum += aa
        
    print(sum)
'''

#方法三

a = int(input("请输入数字："))
b = int(input("请输入相加个数："))
num = 0   
sum = 0
um = ""
for i in range(1,b+1):
    sum = a + sum*10
    num += sum
    if i < b:
        um += str(sum) + "+"
    else:
        um = um +str(sum)
print(f"{um}={num}")