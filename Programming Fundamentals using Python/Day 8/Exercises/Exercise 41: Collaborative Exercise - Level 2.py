'''
Write a higher order function, sum_all() to calculate the sum of elements in a list.
sum_all() – It accepts a list and calculates the sum of the elements in the list based on the conditions being checked in the lambda expressions passed to it.
Only those values satisfying the condition should be included in the sum.

Write the following lambda expressions.

greater: To check whether a given number is greater than 10.
divide: To check whether a given number is divisible by 10 and not greater than 100.
range_of_values: To check whether a given number is between 25 and 50 (Both inclusive).
Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
list_of_nos = [25,26,27,28,29,30,147,187]	499
30
165
list_of_nos = [100,200,300,500,1040]	
'''

# Solution

#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    result_sum = 0 
    for i in data:
        if function(i) :
            result_sum += i 
    return result_sum


list_of_nos= [100,200,300,500,1040]

greater = lambda x: x>10 

divide = lambda x: x<=100 and x%10 == 0 

range_of_values = lambda x: 25 <= x <= 30

#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))
