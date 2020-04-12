# 成绩等级判断
score=int(input("请输入学生成绩："))
grades=("优秀","良好","中","合格","不合格")
if score>=90:
    grade=grades[0]
elif score>=80:
    grade=grades[1]
elif score>=70:
    grade=grades[2]
elif score>=60:
    grade=grades[3]
else:
    grade=grades[4]
print("该生成绩为：",grade)