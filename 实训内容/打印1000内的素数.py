# _*_coding:utf-8_*_

# 打印1000内的素数一行只能输出8个
a = 0
i = 2
for i in range(2, 1000 + 1):    
    j = 2
    for j in range(2, i):       
        if i % j == 0:         #如果i能被j整除，则i不是素数，跳出循环
            break               
    else:
        print(i, end=' ')      #如果i能被j整除，则i是素数
        a += 1
        if a == 8:              #每8个素数打印一行
            print()
            a = 0



