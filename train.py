positive = 0
negative = 0
even = 0
odd = 0
for i in range(5):
    num = int(input("请输入数字："))
    if num > 0:
       positive += 1
    else:
       negative += 1
    if num%2 == 0:
       even += 1
    else:
       odd += 1
print("正数的个数为：",positive)
print("负数的个数为：",negative)
print("偶数的个数为：",even)
print("奇数的个数为：",odd)