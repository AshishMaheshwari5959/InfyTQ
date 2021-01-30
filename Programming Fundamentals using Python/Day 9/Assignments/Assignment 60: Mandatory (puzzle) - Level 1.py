'''
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.


Also write the pytest test cases to test the program.

Sample Input	Expected Output
1122334455ababzzz@@@123#*#*	12345abz@#*
'''

# Solution

#PF-Assgn-60
def remove_duplicates(value):
    string = ""
    for letter in value:
        if letter in  string :
            pass  
        else :
            string += letter 
    return string 

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
