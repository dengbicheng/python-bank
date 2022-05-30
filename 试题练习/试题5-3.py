# _*_coding:utf-8_*_
# @Time : 2022/5/20 15:35
# @Author : 邓必成
# @File :试题5-3.PY

#方法一
'''
num = int(input("请输入一个整数："))
#输出这个整数是几位数
print(f"这是一个{len(str(num))}位数")
while num > 0:
    print(num%10,end="")
    num = num//10
print()
'''


#方法二
str = input("请输入一个差不多8位数的数字:")
print('这个数字是%s位数，逆序为%s'%(len(str),str[::-1]))








        
        
        





    
    
    



