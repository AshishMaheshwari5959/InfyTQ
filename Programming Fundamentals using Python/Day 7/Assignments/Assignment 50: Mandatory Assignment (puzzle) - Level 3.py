'''
Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separ#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    list_words = data.split(" ")
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    temp_list_words = []
    for word in list_words :
        flag = False
        for letter in word :
            if letter not in vowels :
                flag = True
                break
        if flag :
            for letter in word :
                if letter in vowels :
                    word = word.replace(letter,"")
            temp_list_words.append(word)
        else:
            temp_list_words.append(word)
    string = " "
    string = string.join(temp_list_words)
    return string
    
data="I love Python"
print(sms_encoding(data))ately

If a word has only vowels then retain the word as is
If a word has a consonant (at least 1) then retain only those consonants

Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input	Expected Output
I love Python	I lv Pythn
MSD says I love cricket and tennis too	MSD sys I lv crckt nd tnns t
I will not repeat mistakes	I wll nt rpt mstks
'''

# Solution

