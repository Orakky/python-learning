#实例11 养兔子
#题目 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

month=int(input('兔子要繁殖几个月？'))

#初始化兔子个数
month_1 = 1
month_2 = 0
month_3 = 0

month_elder = 0


for i in range(month):
    month_1,month_2,month_3,month_elder=month_elder+month_3,month_1,month_2,month_elder+month_3
    print('第%d个月共'%(i+1),month_1+month-2+month_3+month_elder,'对兔子')
    print('其中1月兔：',month_1)
    print('2月兔：',month_2)
    print('3月兔：', month_3)
    print('成年兔:', month_elder)

