'''
The below function is written to check whether a given three digit number is an Armstrong number.

Hint: An “Armstrong number” is an n-digit number that is equal to the sum of the nth powers of its individual digits.
Example: 371 is an Armstrong number as 371 = 3^3 +7^3+ 1^3

But the function is having errors/bugs, debug the program using the Eclipse debugger and correct it.
'''

# Solution

#PF-Tryout
def find_armstrong(number):
    temp = number
    result = 0
    while(number!=0):
        remainder=number%10
        number=number/10
        result+=(remainder*remainder*remainder)
    if(result==temp):
        return True
    return False

number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")
