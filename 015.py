#实例15 
#分数归档 利用条件运算符：学习成绩>=90的同学用a来表示 60～89用b表示，60以下c表示

points=int(input('输入考试分数：'))

if points>=90:
    grade='A'
elif points<60:
    grade='C'
else:
    grade='B'
print(grade)            