#实例20
#高空抛物 100米高度自由落下 每次落地后跳回原高度的一半 再落下 求它在第10次落地时 共经过多少米？第十次反弹多高？

high=200
total=100

for i in range(10):
    high/=2
    total+=high
    print(high/2)

print("总长：",total)    