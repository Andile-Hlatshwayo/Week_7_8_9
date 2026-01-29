#Sets

#Its an unordered collection of elements
#Does not allow duplicate value unlike Lists or tuples. Can add or remove
#Useful for performing Union, intersection and the difference between collection of elements
# 3 single quotes for commenting  multiple lines
'''print(my_set)
Just like this
'''
my_set={1,2,3,4,5}
#print(my_set)
my_set.add(6)
#print(my_set)
my_set.remove(3)
#print(my_set)

set1={1,2,3}
set2={3,4,5}

#Union
union_set=set1.union(set2)
print(union_set)

#Intersection
inter_set=set1.intersection(set2)
print(inter_set)

#difference
dif_set=set1.difference(set2) #this way and the other way around
print(dif_set)

