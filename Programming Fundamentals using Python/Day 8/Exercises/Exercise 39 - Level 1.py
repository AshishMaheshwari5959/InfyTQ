'''
Write a python lambda expression for calculating simple interest.
If simple interest is greater than 1000, display as “Platinum Member”, otherwise “Gold Member”.

Use the below formula to calculate the simple interest.
simple_interest=(principal_amount*duration in years*rate_of_interest)/100

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
principal_amount = 2000
duration = 2
rate_of_interest = 10	Gold Member
principal_amount = 4000
duration = 12
rate_of_interest = 13	
'''

# Solution

#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest = lambda p,r,t : p*r*t/100 

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    print("Platinum Member")
else:
    print("Gold Member")
