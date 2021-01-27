'''
Write a python program which merges the content of two given lists and sorts the merged list.

Write the following functions to achieve the above functionalities:

def merge_lists(list1,list2): Returns the merged list. Use keyword arguments to pass the lists in method invocation
Note: Merge the lists such that elements in list1 is followed by elements in list2.
Sample Input	Expected Ouput
[1,2,3,4,1]
[2,3,4,5,4,6]	[1,2,3,4,1,2,3,4,5,4,6]

def sort_list(merged_list): Sorts the merged list and returns the sorted list

Sample Input	Expected Ouput
[1,2,3,4,1,2,3,4,5,4,6]	[1,1,2,2,3,3,4,4,4,5,6]
Also write the pytest test cases to test the program.
'''

# Solution

#PF-Exer-29
def merge_lists(list1,list2):
    #Write your logic here
    new_merge_list=[]
    for i in list1:
        new_merge_list.append(i)
    for j in list2 :
        new_merge_list.append(j)
    return new_merge_list

def sort_list(merged_list):
    #Write your logic here
    for i in range (0,len(merged_list)):
        for j in range (i+1,len(merged_list)):
            if merged_list[i]>merged_list[j]:
                merged_list[i],merged_list[j] = merged_list[j],merged_list[i]
    return merged_list

#Provide different values for list1 and list2 and test your program
merged_list=merge_lists(list1=[1,2,3,4,1] ,list2=[2,3,4,5,4,6])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)
