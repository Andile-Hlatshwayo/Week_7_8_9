#Tuples

#its a collection of ordered elements similar to lists
#They are immutable - once they're created, their elements cannot be changed, added or removed
# Which makes it useful for representing fixed collections of items that should not be modified
#Ordered and unchangable and allow duplicates
#-1 gives the last item

my_tuple=(1,2,3,4,5)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

#Concantenation - adding(+) two or more tuples together
#Repetition having one tuple and you can use the multiplication(*) operator to multiply that same tuple

tuple1=(1,2,3)
tuple2=(4,5,6)
conc_tuple=tuple1+tuple2 #Concantenation
print(conc_tuple)

rep_tuple=tuple1*3 #Repetition
print(rep_tuple)