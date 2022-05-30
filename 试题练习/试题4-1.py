# _*_coding:utf-8_*_
# @Time : 2022/5/23 16:17
# @Author : 邓必成
# @File :试题练习4-1.PY

#打印100到999之间的素数

for i in range(100, 1000):  

    for j in range(2, i):   
        if i % j == 0:        #如果i能被j整除，则i不是素数，跳出循环，否则打印i
            break
    else:   
        print(i)


        