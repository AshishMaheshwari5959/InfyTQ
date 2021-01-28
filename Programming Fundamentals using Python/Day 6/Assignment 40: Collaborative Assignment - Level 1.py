'''
Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not. The function should return true, if it is a palindrome. Else it should return false.

Note- Perform case insensitive operations wherever necessary.

Also write the pytest test cases to test the program.
'''

# Solution

#PF-Assgn-40
def is_palindrome(word):
    word = word.lower()
    if len(word) > 1 and word[0] == word[-1] :
        word = word[1:-1]
        is_palindrome(word)
        return True
    elif len(word) <= 1 :
        return True
    else :
        return False

#Provide different values for word and test your program
result=is_palindrome("Malayyalam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
