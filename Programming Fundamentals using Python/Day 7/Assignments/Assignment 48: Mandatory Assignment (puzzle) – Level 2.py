'''
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.

Also write the pytest test cases to test the program.


Sample Input	Expected Output
{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}	[2, 2, 1]
'''

# Solution

#PF-Assgn-48

def find_correct(word_dict):
    #start writing your code here
    correct,almost_correct,wrong = 0,0,0
    result_list = []
    for key,value in word_dict.items() :
        if key == value :
            correct += 1 
        else :
            counter = 0
            temp_lista = []
            temp_listb = []
            for lettera in key :
                temp_lista.append(lettera)
            for letterb in value :
                temp_listb.append(letterb)
            for i in range(0,len(temp_lista)):
                if temp_lista[i] != temp_listb[i] :
                    counter += 1
            if counter <= 2 :
                almost_correct += 1 
            else :
                wrong += 1 
                
    result_list.append(correct)
    result_list.append(almost_correct)
    result_list.append(wrong)
    return result_list

word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))
