my_tuple = ("apple","dog","parrot")

print(my_tuple[2])

print(len(my_tuple))

coordinates=(4,5)
x,y=coordinates

print(x)
print(y)

tuple_con=(1,3,7)

concate=tuple_con + ('lion',5.825)
print(concate)


is_present = 1 in tuple_con
print(is_present)


def coordinates2():
    return(3,4)

x,y = coordinates2()
print(x)
print(y)