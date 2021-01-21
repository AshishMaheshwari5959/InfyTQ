'''
Jack and his three friends have decided to go for a trip by sharing the expenses of the fuel equally.

Write a Python program to calculate the amount (in Rs) each of them need to put in for the complete (both to and fro) journey.
The program should also display True, if the amount to be paid by each person is divisible by 5, otherwise it should display False. (Hint: Use the relational operators in print statement.)

Assume that mileage of the vehicle, amount per litre of fuel and distance for one way are given.

Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
Mileage of the vehicle (km/litre of fuel)	Amount per litre of fuel (Rs)	Distance for one way (kms)	
12	65	96	260.0
True
12	40	190	
'''

# Solution

#PF-Assgn-3
#This verification is based on string match.

mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
per_head_cost = amount_per_litre * distance_one_way * 2 / ( mileage * 4 )
if per_head_cost%5 == 0:
    divisible_by_five=True

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
