#实例14
#分解质因数
#讲一个整数分解成质因数

target=int(input('输入一个整数：'))
print(target,'= ',end='')

if target<0:
    targe=abs(target)
    print('-1*',end='')

flag=0
if target <=1:
    print(target)
    flag=1
    
while True:
    if flag:
        break
    for i in range(2,int(target+1)):
        if target%i==0:
            print("%d"%i,end='')
            if target==i:
                flag=1
                break
            print('*',end='')
            target/=i
            break    
