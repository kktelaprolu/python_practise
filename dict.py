my_dict = {"name":"KK", "age":29, "work":"It"}

print(my_dict['age'])
print(my_dict['work'])

my_dict['age']=30

print(my_dict['age'])
print(my_dict['work'])
print(my_dict)

for key, value in my_dict.items():
    print(key, value)

del my_dict['work']

print(my_dict['age'])
print(my_dict['work'])