'''
Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.
Also write the pytest test cases to test the program.
'''

# Solution

#PF-Assgn-22
def find_leap_years(given_year):
    list_of_leap_years = []
    while len(list_of_leap_years)<15 :
        if (given_year%4 == 0) and (given_year%100!=0):
            list_of_leap_years.append(given_year)
        elif (given_year%400 == 0) :
            list_of_leap_years.append(given_year)
        given_year += 1
    # Write your logic here

    return list_of_leap_years

list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)
