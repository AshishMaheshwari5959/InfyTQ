'''
For the boarding problem, two test cases are already written and given to you.

a) Execute those test cases against the program.

Follow the steps given below in Eclipse Plug-in to execute the test cases:

    Step 1: Inside a package in python project, create a .py file named test_solution.

    Step 2: Copy the pytest test cases given in Starter Testcase tab to test_solution.py file.

    Step 3: In the same package, create a .py file named solution.

    Step 4: Copy the program given in the Starter Code tab to solution.py.

    Step 5: Right click on test_solution.py file and choose Run as -> Python unit-test. The pytest test cases in test_solution.py will be executed     against the program in solution.py and the report will be generated in the console.

    Note:If it gives an error, use the steps in previous page to configure pytest and continue

    Step 6: If there are any failed test cases, debug the program for any logical errors, correct it and test again.
b) Include two test cases to test the logic written for batch number 2. Execute the test cases and in case of any failed test cases, debug, fix the code and test again until all the test cases have passed.


Seat Number	Batch Number
1 to 25	1
26 to 100	2
101 to 200	3
Any other value	-1
'''

# Solution

#PF-Tryout
#Program to be tested

def boarding(seat_number):
    if(seat_number>=1 and seat_number<=25):
        batch_no=1
    elif(seat_number>=26 and  seat_number<=100):
        batch_no=2
    elif(seat_number>=101 and seat_number<=200):
        batch_no=3
    else:
        batch_no=-1
    return batch_no
    
#PF-TCV-Tryout
import pytest
from <packagename>.solution import function_name

def test_boarding_1():
    result=boarding(3)
    assert result==1

def test_boarding_2():
    result=boarding(24)
    assert result==1
