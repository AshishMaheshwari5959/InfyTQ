'''
Complete the code given in the starter code pane based on the comments given in it.
'''

# Solution

#PF-Tryout

def func1():
    result_sum=0
    #Write the code to find the sum of numbers from 1 to 10000000
    print("Sum from func1:",result_sum)

def func2():
    result_sum=0
    #Write the code to accept 5 numbers from user and find its sum
    print("Sum from func2:",result_sum)

#Modify the code given below to execute func1() and func2() in two separate threads
thread1 = Thread(target=func1)
thread1.atart()
thread2 = Thread(target=func2)
thread2.start()
thread1.join()
thread2.join()
