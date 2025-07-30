# for 存储对象元素的变量 in 对象
friends = ['a', 'b', 'c', 'd']
for friend in friends:
    print(friend,end='\t')

movies = {'1': 'a', '2': 'b', '3': 'c', '4': 'd'}
for title in movies.keys():
    print(title)

for i in enumerate(movies.items()):
    print(i)

list1 = [i**2 for i in (1,2,3,4,5,6,7,8,9)]
print(list1)
list2 = []
for i in range(10):
    list2.append(i**2)
print(list2)

list3=['rachel','ross','chandler','joey','monica','phoebe']
list3.sort()
print(list3)
for name in list3:
    name=name.capitalize()
    print(name)

list3=[i.capitalize() for i in list3]
print(list3)
for i in enumerate(list3):
    print(i)