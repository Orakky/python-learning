# 有四个数字：1 2 3 4 能组成多少个不同的互不相同且无重复数字的三位数
total = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)                
