'''
Assume that a poem is given. Write the regular expressions for the following:
Print how many times the letter 'v' appears in the poem.
Remove all the newlines from the poem and print the poem in a single line.
If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.
If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*.
Test your code by using the given sample inputs.
Verify your code by using the 2nd sample input(highlighted) given below:

Sample Input	Expected Output
If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aching,
Or cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.
4

If I can stop one heart from breaking, I shall not live in vain; If I can ease one life the aching, Or cool one pain, Or help one fainting robin Unto his nest again, I shall not live in vain.

If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the aChing,
Or Cool one pain,
Or help one fainting robin
Unto his nest again,
I shall not live in vain.

If I can stop one heart from breaking,
I shall not live in vain;
If I can ease one life the achi*\*
Or cool one pain,
Or help one fai*\*ng robin
Unto hi*\*est again,
I shall not live in vain.
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''

# Solution

#PF-Assgn-53
#This verification is based on string match.
import re
poem='''It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''

#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1
print(len(re.findall(r'v',poem)))

print()
print(re.sub(r'(\n+)(?=[A-Z])', r' ',poem))

print()
print(re.sub(r'ch',r'Ch',re.sub(r'co',r'Co',poem)))

print()
print(re.sub(r'hi...',r'hi*\*',re.sub(r'ai...',r'ai*\*',poem)))
