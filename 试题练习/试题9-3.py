def huiwenchuan(shuru):
    if len(shuru) == 1:
        return True
    elif shuru[0] == shuru[-1] and shuru[1] == shuru[-2]:
        return True
    else:
        return False 
shuru = input("输入一个回文串：")
print(huiwenchuan(shuru))
    

        