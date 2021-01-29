'''
Write a python lambda expression for calculating sum of two numbers and find out whether the sum is divisible by 10 or not.


Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
num1 = 5
num2 = 10	Not Divisible by 10
num1 = 20
num2 = 30	
'''

# Solution

#PF-Exer-40
#This verification is based on string match.

num1=20
num2=30

div = lambda x,y : x+y  

if(div(num1,num2)%10)==0:
    print("Divisible by 10")
else :
    print("Not Divisible by 10")
