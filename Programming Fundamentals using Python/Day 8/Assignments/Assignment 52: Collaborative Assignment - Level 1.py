'''
Consider sample data as follows: sample_data=range(1,11)


Create two functions: odd() and even()
The function even() returns a list of all the even numbers from sample_data
The function odd() returns a list of all the odd numbers from sample_data


Create a function sum_of_numbers() which will accept the sample data and/or a function.
If a function is not passed, the sum_of_numbers() should return the sum of all the numbers from sample_data
If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.
'''

# Solution

#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    list_sum=0
    if filter_func :
        list_of_num = filter_func(list_of_num)
    for i in list_of_num :
        list_sum += i 
    return list_sum

def even(data):
    even_data=[]
    for i in data :
        if i%2==0:
            even_data.append(i)
    return even_data

def odd(data):
    odd_data=[]
    for i in data :
        if i%2!=0:
            odd_data.append(i)
    return odd_data

sample_data = range(1,11)

print(sum_of_numbers(sample_data,None))
print(sum_of_numbers(sample_data,odd))
print(sum_of_numbers(sample_data,even))
