#从键盘接收一个整数 N，统计出 1~N 之间能被 8 整除的整数的个数，以及这些能被 8 整除的数的和。
n = int(input("输入一个整数："))

if not 2 <= n <= 1000:
    print("你的输入有误")

else:
    geshu = 0
    num = 0
    for i in range(1,n+1):
        if i%8 == 0:
            geshu += 1
            num += i
    print(f"1~20 之间能被 8 整除的数的个数：{geshu}\n1~20 之间能被 8 整除的所有数之和：{num}")

        
