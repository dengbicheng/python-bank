n = int(input("请输入一个你要判断的年:"))

if n%400 == 0 or n%4 == 0:
    print(f"{n}是闰年")

else:
    print(f"{n}不是闰年")