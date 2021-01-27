'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program.

Sample Input	Expected Output
AAAABBBBCCCCCCCC	4A4B8C
AABCCA	2A1B2C1A
'''

# Solution

#PF-Assgn-30

def encode(message):
    string = ''
    count = 1
    if len(message)==1 :
        string = '1'+message
    for i in range(0,len(message)-1):
        if message[i] == message[i+1] :
            count += 1 
        else :
            string = string + str(count) + message[i]
            count = 1
        if i+1 == len(message)-1 :
           string = string + '1' + message[i+1]
        
    return string
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
