'''
Write a python function, create_largest_number(), which accepts a list of numbers and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.

Also write the pytest test cases to test the program.

Sample Input	Expected Output
23,34,55	553423
'''

# Solution

#PF-Assgn-36
def create_largest_number(number_list):
    largest_number = 0
    for i in range(0,len(number_list)):
        maximum_number = max(number_list)
        number_list.remove(maximum_number)
        largest_number = largest_number*100 + maximum_number
    return largest_number

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
