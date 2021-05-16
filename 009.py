#实例9
#暂停1s输出
#使用time模块的sleep（）函数
import time

for i in range(1,4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)