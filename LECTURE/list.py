# list = ['a',['b','c'],'d']
# # print(list)
# # print(list[0])
# # print(list[1])
# print(list[1][0])
# del list[0]
# print(list)
# list.insert(0,'a')
# print(list)
# list.append('e')
# print(list)
# list.append(['f','g'])
# print(list)
# list.extend(['h','i'])
# print(list)
# list.reverse()
# print(list)
# list.extend('hello')
# print(list)

list2=[1,2,3,4,5,6,7,8,9,10]
x=list2.pop()
print(x)
print(list2)
list2.remove(9)
print(list2)
list3=list2.copy()
print(list3)
list2.clear()
print(list2)
len(list3)
print(len(list3))
print(list3.count(5))

list4=[4,3,6,2,8,323,63,7]
list4.sort(reverse=True)
print(list4)

list5=[0,6,35,63,555,246,2,63]
list5=sorted(list5)
print(list5)