#输入两个正整数 m 和 n，输出其最大公约数和最小公倍数


m = int(input('请输入第一个正整数：'))
n = int(input('请输入第二个正整数：'))
if m > n:
    m,n = n,m
for i in range(m,0,-1): #从m到1
    if m % i == 0 and n % i == 0: #判断m和n能否被i整除
        print('最大公约数为：',i)
        print('最小公倍数为：',m*n//i)
        break  #如果能被整除输出完成，跳出循环


#方法二：
'''
a = int(input('请输入第一个数: '))
b = int(input('请输入第二个数: '))
Min = min(a, b)  # 返回最小数：
A = 0
for i in range(1, int(Min + 1)):
    if a % i == 0 and b % i == 0:
        A = i
print('最大公约数为：%d' % A)
B = a * b / A
print('最小公倍数为:%d' % B)
'''