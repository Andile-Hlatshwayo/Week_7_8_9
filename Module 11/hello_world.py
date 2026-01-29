#Loops control statements

fruits=["Apple", "Banana", "cherry", "date"]
for fruit in fruits:
    if(fruit=="cherry"):
        break #exits the loop
    print(fruit)  
print()
for fruit in fruits:
    if(fruit=="cherry"):
        continue #skips cherry and moves to the next 
    print(fruit)      
print()
for fruit in fruits:
    if(fruit=="cherry"):
        pass #Placeholder, no action is needed for cherry
    print(fruit)    

