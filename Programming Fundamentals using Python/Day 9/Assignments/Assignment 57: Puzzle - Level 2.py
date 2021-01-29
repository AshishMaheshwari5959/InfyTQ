'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of circular primes less than the given limit.
'''

# Solution

#PF-Assgn-57
def check_prime(number):
    if number == 1 or number == 4 or number == 0 :
        return False
    for i in range(2,int(number/2)) :
        if number%i == 0 :
            return False
    return True 

def rotations(num):
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    rotation_list = []
    if num < 10 :
        rotation_list.append(num)
        return rotation_list
        
    if 9< num < 100 :
        rotation_list.append(num)
        ones = num%10 
        tens = num//10 
        rotation_list.append(ones*10+tens)
        return rotation_list
    
    if 99 < num < 1000:
        rotation_list.append(num)
        ones = num%10 
        tens = (num//10)%10
        hundred = num//100 
        rotation_list.append(ones*10+tens*100+hundred)
        rotation_list.append(ones*100+tens+hundred*10)
        return rotation_list
        
def get_circular_prime_count(limit):
    prime_list = []
    for i in range(0,limit) :
        if check_prime(i) :
            prime_list.append(i)
    
    counter = 0 
    final_list = []
    for i in prime_list :
        temp_list = rotations(i)
        flag = False
        for j in temp_list:
            if not check_prime(j):
                flag = True 
        if flag==False:
            counter = counter + 1
            final_list.append(i)
    return counter
    
#Provide different values for limit and test your program
print(get_circular_prime_count(1000))
