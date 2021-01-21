'''
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Estimated time: 15 minutes

Sample Input	Expected Output
heads-150 legs-400	100 50
heads-3 legs-11	No solution
heads-3 legs-12	0 3
heads-5 legs-10	5 0
'''

# Solution

#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if heads > legs or legs < 2*heads or heads*legs == 0 or legs%2 != 0 :
        print(error_msg)
    else :
        rabbit_count = (legs - 2*heads)/2
        chicken_count = heads - rabbit_count
        if rabbit_count.is_integer and chicken_count.is_integer:
            print(int(chicken_count),int(rabbit_count))
        else :
            print(error_msg)       

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(38,131)
