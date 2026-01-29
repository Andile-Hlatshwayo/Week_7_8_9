#Functions (method)

# It is a fundamental way to structure your code.
# Allow you to encapsulate your code and reuse it throuhtout your program

def greet(name):
    print(f"Hello, {name}")
greet('Andile')

def add(a,b):
    return a**b
result=add(2,5)
print(result)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)    
        
def greetings(name,greeting="Hello"):
    print(f"{greeting}, {name}")
greetings("Hive") 
greetings("Hive","Good morning")   #Yes we did say greeting is "Hello" but when we now put another value when we call the function it now changes