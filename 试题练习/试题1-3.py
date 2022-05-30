
#创建一个函数判断这个数是不是素数
def pandansushu(num):
    if num < 2:
        print("输入的数不能小于2!")
    for i in range(2,num):
        if num % i == 0:
            break

    print("这个数是素数")
num = int(input("输入一个整数这个数不能小于2："))
pandansushu(num)