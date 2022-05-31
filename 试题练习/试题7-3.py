for a in range(100,816-100):
    x = a//100
    y = a%100//10
    z =a%10

    b = 816-a
    x2 = b // 100
    y2 = b // 10 % 10
    z2 =b % 10
    if y ==x2 and z==y2 and z==z2:
        print(f"x:{x},y:{y},z:{z},{a}+{b}=816")
        break