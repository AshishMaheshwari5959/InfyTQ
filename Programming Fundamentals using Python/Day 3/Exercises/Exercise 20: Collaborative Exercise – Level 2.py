'''
For the boarding problem, check the coverage and correctness for the test cases you have written.

Follow the steps given below in Eclipse Plug-in to check the coverage of the test cases:

    Step 1: Inside a package in python project, create two .py files named test_solution and solution.

    Step 2: Copy the code from Starter Testcase tab to test_solution.py file and follow the instructions provided in the code.

    Step 3: Copy the code from Starter Code tab to solution.py and follow the instructions provided in the code.

    Step 4: Right click on test_solution.py file and choose Run as -> Python unit-test. The pytest test cases in test_solution.py will be executed     against the program in solution.py and the report will be generated in the console.

    Step 5: Choose test_solution.py file and click on verify. A pop-up containing coverage and correctness report will be generated.

   Step 6: If the coverage is less than 100%, add the remaining test cases/make the necessary corrections in the solution based on the     coverage report.

    Step 7: If there are any incorrect test cases as per correctness report, make the necessary corrections.

    Step 8: Repeat Steps 4,5, 6 and 7 until coverage is 100% and all test cases are correct.

    Step 9: You can also verify the program against actual test cases and ensure that the program is logically correct.
'''

#Solution

def boarding(seat_number):
    if(seat_number>=1 and seat_number<=25):
        batch_no=1
    elif(seat_number>=26 or  seat_number<=100):
        batch_no=2
    elif(seat_number>=101 and seat_number<=200):
        batch_no=3
    else:
        batch_no=-1
    return batch_no
    
import pytest
from <packagename>.solution import function_name

def test_boarding_1():
    result=boarding(3)
    assert result==1

def test_boarding_2():
    result=boarding(24)
    assert result==1
