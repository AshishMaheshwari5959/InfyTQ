'''
Write a python function, check_anagram() which accepts two strings and returns True, if one string is an anagram of another string. Otherwise returns False.

The two strings are considered to be an anagram if they contain repeating characters but none of the characters repeat at the same position. The length of the strings should be the same.

Also write the pytest test cases to test the program.

Note: Perform case insensitive comparison wherever applicable.

Sample Input	Expected Output
eat, tea	True
backward,drawback	False
(Reason: character 'a' repeats at position 6, not an anagram)
Reductions,discounter	True
About, table	False
'''

# Solution

#PF-Assgn-54
import re
def check_anagram(data1,data2):
    if len(data1) != len(data2):
        return False
    for i in range(0,len(data2)):
        if data1[i] == data2[i]:
            return False
    d1={}
    d2={}
    for i in data1:
        d1[i]=1
    for i in data2:
        d2[i]=1
    if d1!=d2 :
        return False
    return True

print(check_anagram("eat","tea"))
