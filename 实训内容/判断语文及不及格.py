# _*_coding:utf-8_*_

""" 这里没必要加注释，看不懂埋了吧 """

#判断语文成绩档位
a = int(input("请输入你的语文成绩："))
if a<60:
    print("D档")
elif 60<=a<80:
    print("C档")
elif 80<=a<90:
    print("B档")
elif a>=90:
    print("A档")
