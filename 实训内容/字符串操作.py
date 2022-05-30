# _*_coding:utf-8_*_
s= ' Optimization analysison iteration process of complex productdevelopment based on uncertainty'

#统计这个字符串中的单词数
print(f"字符串中有{len(s.split())}个单词")

#去掉字符串中的空格
print("去掉空格后：",s.replace(' ',''))

#将字符串中的单词变成大写
print("转换为大写后：",s.upper())

#求“a”第一次出现的位置
print("第一次出现的为置为：",s.find('a'))

#求“a”最后出现的位置
print("最后出现的为置为：",s.rfind('a'))

#输出“of”之后的内容
print("输出of之后的内容：",s.split('of')[1])

