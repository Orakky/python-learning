#浅拷贝 深拷贝
import copy

list1=[1,2,3,['a','b']]

list2 = list1 #赋值
list3 = list1[:]#浅拷贝
list4 = copy.copy(list1)#浅拷贝
list5 = copy.deepcopy(list1)#深拷贝

print("-------ONE------")
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

list1.append(4)


print("------TWO------")
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

list1[3].append('c')

print("-------THREE------")
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)