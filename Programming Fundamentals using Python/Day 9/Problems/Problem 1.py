'''
Write a python function to add 'ing' at the end of a given string and return the new string.
If the given string already ends with 'ing' then add 'ly'.
If the length of the given string is less than 3, leave it unchanged.

Sample Input	Expected Output
sleep	sleeping
amazing	amazingly
is	is
'''

# Solution

#PF-Prac-1
def add_string(str1):
  if len(str1) > 2 :
      if str1[-3:] == 'ing':
          str1 += 'ly'
          return str1
      str1 += 'ing'
      return str1
  return str1

str1="com"
print(add_string(str1))
