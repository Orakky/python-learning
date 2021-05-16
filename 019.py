#实例19 完数
# 一个数恰好等于它的因子之和 例如 6=1+2+3。
#找出1000以内的所有完数

def factor(num):
    target=int(num)
    res=set()
    for i in range(1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res


for i in range(2,1001):
    if i == sum(factor(i))-i:
        print(i)    
