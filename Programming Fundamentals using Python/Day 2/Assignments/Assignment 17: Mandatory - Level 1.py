'''
An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5.
Hike percentage based on job levels are given below:


Job level	Hike Percentage (applicable on current salary)
3	15
4	7
5	5
In case of invalid job level, consider hike percentage to be 0.


Given the current salary and job level, write a python program to find and display the new salary of an employee. Identify the test data and use it to test the program.
'''

# Solution

#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    if job_level == 3 :
        hike_percentage = 15
    elif job_level == 4 :
        hike_percentage = 7
    elif job_level == 5 :
        hike_percentage = 5 
    else :
        hike_percentage = 0 
        
    new_salary = current_salary + current_salary*hike_percentage/100

    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)
