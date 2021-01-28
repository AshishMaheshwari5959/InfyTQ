'''
Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
Handle the possible errors in the code written inside the function.

Sample Input	Expected Output
16	120
'''

# Solution

#PF-Assgn-43

def find_smallest_number(num):
    #start writing your code here
    result = 1 
    while result > 0 :
        list_of_divisors = []
        for j in range(1,result+1):
            if result%j == 0 :
                list_of_divisors.append(j)
        if len(list_of_divisors) == num :
            return result
        result += 1

num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
