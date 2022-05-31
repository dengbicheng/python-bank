#使用冒泡排序法对列表中的整数按升序进行排序

a=[1,9,3,7,4,2,5,0,6,8]
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

