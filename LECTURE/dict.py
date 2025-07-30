dict={'s':10,'t':99,'y':0,'o':78,'x':6}
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get('s'))

for key,value in dict.items():
    print(key,value)

print(dict.pop('o'))
print('s' in dict)
print(dict.popitem())

dict2={'h':45,'jk':78}
# dict=dict(zip(dict,dict2))
# print(dict)
merged_dict = dict|dict2
print(merged_dict)