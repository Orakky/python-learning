#实例13
#水仙花数
for i in range(100,1000):
    s = str(i)
    one = int(s[-1])
    two = int(s[-2])
    three = int(s[-3])
    if i == one**3 + two**3 + three**3:
        print(i)

    