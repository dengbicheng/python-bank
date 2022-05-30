# _*_coding:utf-8_*_
# @Time : 2022/5/23 15:27
# @Author : 邓必成
# @File :试题5-1.PY

#while循环
a = 1
while a<8:
    print("*"*a)
    a += 2

#for循环
for j in range(1,8,2):
    print("*"*j)


#用户输入
s = int(input("请输入你要打印的层数:"))
i = 1
while i-s <= s:

    j = 1
    while j<= i:
        print("*",end="")
        j +=1
    print()
    i += 2