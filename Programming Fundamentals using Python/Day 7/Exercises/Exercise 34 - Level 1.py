'''
We have ‘N’ flavors of toppings that can be added to a coffee. For example  chocolate, hazelnut, vanilla, Irish and so on.

Write a function that takes the number of available flavors as input and returns the total number of different ways we can have our coffee. Note that we can have coffee without any toppings or with different combination of toppings.
 '''
 
 # Solution
 
 #PF-Exer-34
import math

def find_number_of_combination(number_of_flavours):
    total_combination=0
    #write your logic here
    for i in range(0,number_of_flavours+1):
        total_combination += math.factorial(number_of_flavours)/(math.factorial(number_of_flavours-i)*math.factorial(i))
    return total_combination

#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)
