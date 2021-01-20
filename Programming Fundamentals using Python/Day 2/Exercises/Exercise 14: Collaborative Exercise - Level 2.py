'''
A teacher in a school wants to find and display the grade of a student based on his/her percentage score. The criterion for grades is as given below:

Score (both inclusive)	Grade
Between 80 and 100	A
Between 73 and 79	B
Between 65 and 72	C
Between 0 and 64	D
Any other value	Z
Assume that the percentage score is a whole number.

Write a python program for the above requirement. Identify the test data and use it to test the program.
'''

#Solution

score = 43
if (80<= score <=100):
    print("A")
elif (73<= score <=79):
    print("B")
elif (65<= score <=72):
    print("C")
elif (0<= score <=64):
    print("D")
else :
    print("Z")
