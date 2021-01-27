'''
Write a python program to display all the common characters between two strings. Return -1 if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.



Sample Input	Expected output
"I like Python"
"Java is a very popular language"	lieyon
'''

# Solution

#PF-Assgn-33

def find_common_characters(msg1,msg2):
    string = ''
    for character1 in msg1 :
        if character1 in msg2 and character1 != ' ' and character1 not in string :
            string += character1
    
    if len(string) == 0 :
        return -1

    return string

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
