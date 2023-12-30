a=10
b=3
sum = a+b
diff = a-b
mul = a*b
div = a/b
print("sum of two numvers:", sum)
print("subtraction of two numvers:", diff)
print("product of two numvers:", mul)
print("queotient of two numvers:", div)

greater_than = a>b
less_than = a<b
lessthan_equl = a<=b
greaterthan_equal = a>b
equal_to = a==b
not_equal = a!=b

print("a is greater than b", greater_than)
print("a is less than b", less_than)
print("a is greater than or equal to b", greaterthan_equal)
print("a is less than or equal to b", lessthan_equl)
print("a is not equal to b", not_equal)


x=True
y=False

and_operator = x and y
or_operator = x or y
not_x = not x  
not_y = not y

print("and operator :", and_operator)
print("or operator :", or_operator)
print("x not operator :", not_x)
print("y not operator :", not_y)


total=10

total+=5
print(total)

total-=5
print(total)

total*=10
print(total)

total/=10
print(total)

my_list = [1,5,2,9,4,69]
a = 5

if a in my_list:
    print(f'{a} is in my_list')
else:
    print(f"{a} is not in my_list")

if a is my_list[1]:
    print(f'{a} is same as my_list[1]')
else:
    print(f'{a} is not same as my_list[1]')

v=a in my_list
print(v)
k=a is my_list
print(k)