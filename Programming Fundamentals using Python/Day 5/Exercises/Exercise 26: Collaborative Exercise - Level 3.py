'''
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself.
145 is a Strong number as 1! + 4! + 5! = 145.

Sample Input	Expected Output
num_list = [145,375,0,100,2]	[145, 2]Note: 0!=1
'''

# Solution

#PF-Exer-26

def factorial(number):
    result = 1
    while number > 0 :
        result *= number
        number = number - 1
    return result


def find_strong_numbers(num_list):
    strong_num_list=[]
    for i in range(0, len(num_list)):
        sum_no = 0 
        temp = num_list[i]
        while num_list[i] > 0 :
            remainder = num_list[i]%10
            sum_no = sum_no + factorial(remainder)
            num_list[i] = num_list[i]//10
        
        if sum_no == temp and temp != 0 :
            strong_num_list.append(temp)
    
    return strong_num_list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
