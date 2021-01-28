'''
Write a python program to guess the number in the user's mind.

randrange function of random module can be used to guess the number in user’s mind.

Note: User should think of a number which is in between 1 and 10 (both inclusive).

Random Range values	Sample number in user’s mind	Number guessed	Expected Output
1 to 10	5	3	Number is low
7	Number is high
5	You have got it right!!!
'''

# Solution

#PF-Tryout
import random
def guess_number(number_in_mind):
    x,y = 1,10
    z = random.randrange(x,y)
    if number_in_mind > z :
        print ('Number is low')
    elif number_in_mind < z :
        print ('Number is high')
    else:    
        print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_number(4)
