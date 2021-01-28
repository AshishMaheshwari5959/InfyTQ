'''
A 10-substring of a number is a substring of its digits that sum up to 10.

For example, the 10-substrings of the number 3523014 are:
3523014, 3523014, 3523014, 3523014

Write a python function, find_ten_substring(num_str) which accepts a string and returns the list of 10-substrings of that string.

Handle the possible errors in the code written inside the function.

Sample Input	Expected Output
'3523014'	['5230', '23014', '523', '352']
'''

# Solution

#PF-Assgn-41
def find_ten_substring(num_str):
    result_list=[]
    for i in range(0,len(num_str)):
        sum10 = 0
        counter = i 
        temp = i
        while sum10 < 10 :
            sum10 += int(num_str[temp])
            counter = counter + 1
            if temp < len(num_str)-1:
                temp = temp + 1
            else:
                break
        if sum10 == 10 :
            result_list.append(num_str[i:counter])
            if (counter<=len(num_str)-1) and (num_str[counter]=='0') :
                result_list.append(num_str[i:counter+1])
            elif num_str[i-1] == '0' and i != 0 :
                result_list.append(num_str[i-1:counter])
    return result_list

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
