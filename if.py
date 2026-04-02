score=int(input("请输入您的成绩:"))
if score>=90:
    print("成绩等级：优秀")
elif score>=80 and score<90:
    print("成绩等级：良好")
elif score>=70 and score<80:
    print("成绩等级：中等")
elif score>=60 and score<70:
    print("成绩等级：及格")
elif  score<60:
    print("成绩等级：不及格")

if score>=60:
    print("恭喜通过考试")
else:
    print("请参加补考")