#Python Syntax
#ex1
#print("Hello World")
#ex2
'''if 5>2:
    print("YES")
'''
#Python Comments
#ex1
#This is a comment
#ex2
'''
This is a comment
written in 
more than just one line
'''
#Python Variables
#ex1
'''carname = "Volvo"'''
#ex2
'''x=5'''
#ex3
'''
x=5
y = 10
print(x+y)'''
#ex4
'''
x=5
y = 10
z=x+y
print(z)'''
#ex5
'''
x,y,z = "Orange", "Banana", "Cherry"
'''
#ex6
'''
x=y=z = "Orange"
'''
#ex7
''' 
def myfunc():
global x
x = 'fantastic'
''' 
#Python Data Types
#ex1
''' 
x=5
print(type(x))

Output: int
''' 
#ex2
'''  
x = "Hello World"
print(type(x))

Output: str
''' 
#ex3
'''
x= 20.5
print(type(x))

Output: float
'''
#ex4
'''
x = ["apple", "banana", "cherry"]
print(type(x))

Output: list
'''
#ex5
'''
x = ("apple", "banana", "cherry")
print(type(x))

Output: tuple
'''
#ex6
'''
x = {"name" : "John", "age" : 36}
print(type(x))

Output: dict
'''
#ex7
'''
x = True
print(type(x))

Output: bool
'''
#Python Numbers
#ex1
'''
x=5
x = float(x)
'''
#ex2
'''
x=5.5
x = int(x)
'''
#ex3
'''
x=5
x = complex(x)
'''
#Python Strings
#ex1
'''
x = "Hello World"
print(len(x))
'''
#ex2
'''
txt = "Hello World"
x = txt[0]
'''
#ex3
'''
txt = "Hello World"
x = txt[2:5]
'''
#ex4
'''
txt = " Hello World "
x = txt.strip()
'''
#ex5
'''
txt = "Hello World"
x = txt.upper()
'''
#ex6
'''
txt = "Hello World"
x = txt.lower()
'''
#ex7
'''
txt = "Hello World"
x = txt.replace('H','J')
'''
#ex8
'''
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
'''
