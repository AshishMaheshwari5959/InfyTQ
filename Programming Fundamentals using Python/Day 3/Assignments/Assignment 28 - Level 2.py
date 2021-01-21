'''
Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.

Always num1 should be less than num2
Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
Sum of the digits of the number is a multiple of 3
Number has only two digits
Number is a multiple of 5
Display the maximum element from the list
In case of any invalid data or if the list is empty, display -1.
'''

# Solution

#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    if num1>=num2 :
        return max_num
    for i in range(num1, num2+1):
        if i%3==0 and i%5==0 and i<100:
            max_num=i
    # Write your logic here
    return max_num

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
