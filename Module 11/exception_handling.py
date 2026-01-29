#Exception handling allows a programmer to deal with runtime errors or exceptions
#An exception is an event that occurs during the execution of a program disrupting the  normal flow of a program's execution
# try and except blocks are used for exception handling
#try block contains the code that may raise an exception
#except block contains the code that will execute if an exception occurs

'''Lesson 1

try:
    print(x)
#except NameError:
#    print("Variable x is not defined")
except:
    print("An exception occured")  
finally:
    print("The 'try except' is finished")      
    '''
     
#Lesson 2

try:
    print(x)
except NameError:
    print("Variable x is not defined")  
else:
    print("Everything went wrong")
    
    
x=-1
if x<0:
    raise Exception("Sorry, no numbers below zero")  #This exception is triggered when a condition is met
           