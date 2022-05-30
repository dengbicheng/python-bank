# _*_coding:utf-8_*_

list = [12,21,'python',77,86,33.6,{'name':'Jack'},'66',88]
print("输出原列表")
print(list)

#保留列表中的整数
for i in range(len(list)-1,-1,-1):  #从后往前遍历
    
    if not isinstance(list[i],int):  #判断是否是整数
        
        del list[i]              #删除不是整数的元素

list.sort(reverse=True)     # 降序排列
print("保留列表中的整数后降序的列表")
print(list)