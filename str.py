intnumben = 0
strnumben = 0
negative = 0
even = 0
for i in range(5):
    a = input("请输入随便你想输入的数据类型：")
    try:
        num = int(a)
        intnumben += 1
        if num > 0:
            even += 1
        elif num < 0:
            negative += 1
    except:
        try:
            num = float(a)
            if num.is_integer():
                intnumben += 1
                num = int(num)
            if num > 0:
                even += 1
            elif num < 0:
                negative += 1
        except:
              strnumben += 1


print("字符串的个数为：",strnumben)
print("整数的个数为：",intnumben)
print("正数的个数为：",even)
print("负数的个数为：",negative)

