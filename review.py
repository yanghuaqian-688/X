while True:
    print("\n简易计算器\n")
    print("1,加法")
    print("2,减法")
    print("3,乘法")
    print("4,除法")
    print("0,退出")

    choice=input("请选择功能:")

    if choice=="0":
        print("已经退出计算器")
        break
    if choice not in ["1", "2", "3", "4"]:
        print("输入错误，请重新选择")
        continue

    a=float(input("请输入第一个数："))
    b=float(input("请输入第二个数："))

    if choice=="1":
        print("结果是：",a+b)

    elif choice=="2":
        print("结果是：",a-b)

    elif choice=="3":
        print("结果是",a*b)
    elif choice=="4":
         if b==0:
            print("除数不能为零")
         else:
            print("结果是",a/b)

    input("按回车继续")
