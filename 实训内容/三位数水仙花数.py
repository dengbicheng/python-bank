# _*_coding:utf-8_*_
#打印一个三位数的水仙花数
for i in range(100,1000):
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if i == a**3 + b**3 + c**3:
        print(i)
        
