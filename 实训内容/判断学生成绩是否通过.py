# _*_coding:utf-8_*_

""" 这里没必要加注释，看不懂埋了吧 """

#判断学生成绩是否通过
x,y,z = map(int,input("请输入你的语文，数学，英语成绩（注意用空格分开）：").split(" "))
if x and y and z >= 60:
    print("通过")
else:
    print("未通过")





