# _*_coding:utf-8_*_
# @Time : 2022/5/23 16:17
# @Author : 邓必成
# @File :试题练习4-2.PY

#方法一
'''
#输入一行字符，输出其中的数字和字母的个数。
shuru = input("请输入一行字符：")
num = 0
low = 0
for i in shuru:
    if i.isdigit():     #isdigit()判断是否是数字
        num += 1
    elif i.islower():   #islower()判断是否是小写字母
        low += 1
    elif i.isupper():   #isupper()判断是否是大写字母
        low += 1
print(f"数字个数为{num}个，字母个数为{low}个")
'''


'''
#方法二
a = ["1","2","3","4","5","6","7","8","9","0"]
b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
c = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
shuru = input("请输入一行字符：")
num = 0
low = 0
for i in shuru:
    if i in a:
        num += 1
    elif i in b:
        low += 1
    elif i in c:
        low += 1
print(f"数字个数为{num}个，字母个数为{low}个")
'''



#方法三
shuru = input("请输入一行字符：")
num = 0
low = 0
for i in shuru:
    if "a"<= i <= "z":
        low += 1
    elif "0" <= i <= "9":
        num += 1
    elif "A" <= i <= "Z":
        low += 1
print(f"数字为{num},字母个数为{low}")
