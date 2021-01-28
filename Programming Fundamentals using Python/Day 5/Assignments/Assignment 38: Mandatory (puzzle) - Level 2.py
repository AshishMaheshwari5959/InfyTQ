'''
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.

The number and its double should have exactly the same number of digits.
Both the numbers should have the same digits ,but in different order.
Otherwise it should return False.

Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.
'''

# Solution

#PF-Assgn-38

def check_double(number):
    len1 = 0
    number1 = number
    while number1 > 0 :
        len1 += 1
        number1 = number1 // 10
    len2 = 0
    number2 = 2*number
    while number2 > 0 :
        len2 += 1
        number2 = number2 // 10
    if len1 == len2 :
        frequency1 = [0]*10
        frequency2 = [0]*10
        number1 = number 
        number2 = 2*number
        while number1 > 0 :
            remainder = number1%10
            frequency1[remainder] += 1 
            number1 = number1//10
        while number2 > 0 :
            remainder = number2%10
            frequency2[remainder] += 1 
            number2 = number2//10
        if frequency2 == frequency1:
            return True
        else :
            return False
    else :
        return False
#Provide different values for number and test your program
print(check_double(125874))
