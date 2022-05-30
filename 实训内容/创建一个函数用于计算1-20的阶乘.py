# _*_coding:utf-8_*_

#计算阶乘一次输出1-20的阶乘
def actorial(n):                #数学不好也不多解释了
    if n == 1:
        fac = 1
    else:
        fac = n*actorial(n-1)
    return fac

for i in range(1,21):
    print(f"{i}的阶乘为 {actorial(i)}")


