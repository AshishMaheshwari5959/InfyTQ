'''
There are two basketball teams (Team1 and Team2) in a school and they play some matches everyday depending on their time and interest. Some days they play 3 matches, some days 2, some days 1 etc.

Write a python function, find_winner_of_the_day(), which accepts the name of the winner of each match and returns the name of the overall winner of the day. In case of equal number of wins, return “Tie”.

Test your code by using the given sample inputs and verify your code by using the 2nd sample input given below:

Sample Input	Expected Output
("Team1","Team2","Team1")	Team1
("Team1","Team2","Team2","Team1","Team2")
'''

# Solution

#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    t1,t2 = 0,0
    for i in match_tuple :
        if i == "Team1":
            t1 += 1 
        else :
            t2 += 1 
    if t1==t2 :
        return "Tie"
    elif t1>t2 :
        return "Team1"
    else :
        return "Team2"

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2")	)
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
