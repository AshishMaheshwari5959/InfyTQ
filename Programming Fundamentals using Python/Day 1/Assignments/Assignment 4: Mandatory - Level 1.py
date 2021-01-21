'''
Write a Python program to calculate and display the interest on a loan amount (Rupees) using the formula:
interest=(principal * rate of interest * time)/100

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
Principal	Rate of Interest	Time	
20000	5	10	10000.0
7800	7.7	26	
'''
# Solution

#PF-Assgn-4
#This verification is based on string match.

principal=7800
rate_of_interest=7.7
time=26
interest=0

#Start writing your code from here
#Populate the variable: interest
interest=(principal * rate_of_interest * time)/100


#Do not modify the below print statement for verification to work
print(interest)
