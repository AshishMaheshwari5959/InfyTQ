'''
Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and returns the encrypted message.
Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change

Note: 

Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Also write the pytest test cases to test the program.

Sample Input	Expected Output
the sun rises in the east	eht snu sesir ni eht stea
'''

# Solution

#PF-Assgn-47
def encrypt_sentence(sentence):
    #start writing your code here
    list_words = sentence.split(" ")
    for i in range(0,len(list_words),2):
        list_words[i] = list_words[i][::-1]
    for i in range(1,len(list_words),2):
        vowels=['a','e','i','e','u','A','E','I','O','U']
        vowel_list=[]
        consonant_list=[]
        for letter in list_words[i] :
            if letter in vowels :
                vowel_list.append(letter)
            else :
                consonant_list.append(letter)
        list_words[i] = "".join(consonant_list)+"".join(vowel_list)
    final_string = ""
    for word in list_words :
        final_string = final_string + word + " "
    return final_string

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
