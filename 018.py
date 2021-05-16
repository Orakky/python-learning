#实例18 复读机相加
#s=a+aa+aaa+aaaa+aa....a的值，其中a是一个数字
#程序分析 由字符串解决

a=input('被相加数字： ')
n=int(input('相加几次？ '))
res=0
for i in range(n):
    res+=int(a)
    a+=a[0]
print('结果是：',res)