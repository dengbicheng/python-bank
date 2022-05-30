#定义两个函数将小写字母转换为大写字母，大写字母转换为小写字母

a = input("请输入你要转换的英文：")

def xiaoxie(a):
    b = a.lower()
    return b        #返回b的值下面也是如此
def daxie(a):
    b = a.upper()
    return b

print(f"大写内容为{daxie(a)}")
print(f"小写内容为{xiaoxie(a)}")

#把一串英文是大写转小写，小写转大写
b = a.swapcase()
print(f"转换后的内容为{b}")


