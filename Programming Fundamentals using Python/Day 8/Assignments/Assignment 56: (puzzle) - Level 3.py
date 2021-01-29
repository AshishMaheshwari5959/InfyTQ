'''
Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a single space between the words.
Perform case insensitive string comparisons wherever necessary.

Sample Input	Expected Output
"Work like you do not need money love like you have never been hurt and dance like no one is watching"	like 3
"Courage is not the absence of fear but rather the judgement that something else is more important than fear"	fear 2
'''

# Solution

#PF-Assgn-56

def max_frequency_word_counter(data):
    word=""
    frequency=0

    #start writing your code here
    #Populate the variables: word and frequency
    data = data.lower()
    word_list = data.split(" ")
    dict_word = {}
    
    for word in word_list:
        if word in dict_word.keys():
            dict_word[word] += 1 
        else :
            dict_word[word]=1
            
    for key,value in dict_word.items():
        if value>frequency:
            frequency = value
    
    dict_word_2 = {}
    for key,value in dict_word.items():
        if value == frequency:
            dict_word_2[key] = value 
    
    dict_word_3 = {}
    for key,value in dict_word_2.items():
        dict_word_3[key] = len(key) 
        
    maximum_length = 0
    for key,value in dict_word_3.items():
        if value>maximum_length:
            maximum_length = value
    
    dict_word_4 = {}
    for key,value in dict_word_3.items():
        if value == maximum_length:
            dict_word_4[key] = value 
    #print(dict_word)
    #print(dict_word_2)
    #print(dict_word_3)
    #print(dict_word_4)
    for key,value in dict_word_4.items():
        word = key
    print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money love like you have never been hurt and dance like no one is watching"
max_frequency_word_counter(data)
