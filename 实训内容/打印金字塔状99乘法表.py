# _*_coding:utf-8_*_

for i in range(1,10):
    print(" "*int((60-6*i)/2),end=" ")  #每行打多印个空格
    for j in range(1,i+1):
        print(f"{j}x{i}={i*j}",end=" ")
    print() #换行

#将九九乘法表写入TXT文件
with open("九九乘法表.txt","w") as f:
    for i in range(1,10):
        f.write(" "*int((60-6*i)/2))  #将每行打多个空格写入文件 （注意不接受end=""）
        for j in range(1,i+1):
            f.write(f"{j}x{i}={i*j}"+" ")
        f.write("\n") #换行