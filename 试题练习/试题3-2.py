# _*_coding:utf-8_*_
# @Time : 2022/5/23 16:17
# @Author : 邓必成
# @File :试题3-2.PY

shuru = input("请输入一行字符串：")
low = 0
for i in shuru:
    if i.isalpha():     #如果i是小写字母，则low加1  
        low += 1
    elif i.isupper():   #如果i是大写字母，则low加1
        low += 1
print("字母的个数为：",low)
    