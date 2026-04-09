def check(num):
    if num % 2 == 0:
        return "这是偶数"
    else:
        return "这是奇数"

a=int(input("请输入数字："))
print(check(a))


