'''
Write a python function, nearest_palindrome() which accepts a number and returns the nearest palindrome greater than the given number.
Also write the pytest test cases to test the program.


Sample Input	Expected Output
12300	12321
12331	12421
'''

# Solution

#PF-Assgn-46
import math
def nearest_palindrome(number):
    #start writitng your code here
    while number > 0 :
        if str(number) == str(number)[::-1] :
            return number
        number += 1 

number=12300
print(nearest_palindrome(number))
