#1
'''def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = []
num = input("Enter numbers to multiply: ").split()
for i in num:
    numbers.append(int(i))
result = multiply(numbers)
print("Result:", result)'''

#2
'''def count(string):
    upper=0
    lower =0
    for i in string:
        if i.isupper():
            upper +=1
        if i.islower():
            lower +=1
    return upper, lower

string = input()
upper, lower = count(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
'''
#3
'''def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while right>= left:
        if  string[left] != string[right]:
            return False
        left += 1
        right -= 1   
    return True
s = str(input())
print(isPalindrome(s))'''
#4
'''import time
import math
def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    square_root = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {square_root}")

number = int(input())
milliseconds = int(input())

calculate_square_root(number, milliseconds)'''
#5
'''def all(tuple_data):
    for tup in tuple_data :
        if not tup:
            return False
    return True
tuple_data = ()
tup = input("Enter a tuple: ")
tuple_data = tuple(tup.split())
print(all(tuple_data))'''