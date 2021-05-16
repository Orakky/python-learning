#实例30 回文数

n=input("输入一个正整数：")

a=0

b=len(n)-1
flag = True
while a<b:
    if n[a]!=n[b]:
        print('不是回文数！')
        flag = False
        break
    a,b=a+1,b-1

if flag:
    print('是回文数！')    