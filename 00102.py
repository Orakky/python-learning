# 有四个数字：1 2 3 4 能组成多少个不同的互不相同且无重复数字的三位数
import itertools

sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)
