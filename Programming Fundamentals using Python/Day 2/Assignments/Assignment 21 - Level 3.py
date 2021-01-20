'''
Write a python program to generate and display the next date of a given date.

Assume that
Date is provided as day, month and year as shown in below table.
The input provided is always valid. Output should be day-month-year.
Hint: print(day,"-",month,"-",year) will display day-month-year

Sample Input	Expected Output
Day	1	2-9-2015
Month	9
Year	2015

Also identify the test data and use it to test the program.
'''

#Solution

#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    if month == 2 and day == 28 :
        if ( year%4 == 0 and year%100 != 0 ) :
            next_day,next_month,next_year =29,2,year
        elif year%400 == 0 :
            next_day,next_month,next_year =29,2,year
        else :
            next_day,next_month,next_year =1,3,year
            
    elif day == 31 and month == 12 :
        next_day,next_month,next_year =1,1,year+1
    
    elif day == 31 :
        next_day,next_month,next_year =1,month+1,year
    
    elif day == 30 and ( month == 4 or month == 6 or month == 9 or month == 11 ) :
        next_day,next_month,next_year =1,month+1,year
        
    else :
        next_day,next_month,next_year =day+1,month,year
        

    print(next_day,"-",next_month,"-",next_year)


generate_next_date(28,2,2012)
