set1={1,2,3}
set2={1,3,4,5,6}

union = set1.union(set2)
intersection = set1.intersection(set2)
difference_Set=set1.difference(set2)

print(union)
print(intersection)
print(difference_Set)

is_subset=set1.issubset(set2)
is_superset=set1.issuperset(set2)

print(is_subset)
print(is_superset)

my_set ={7,4,9,0}
my_set.add(6)
print(my_set)
my_set.remove(4)
print(my_set)