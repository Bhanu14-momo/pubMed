#Basic Level
#Create a list of 10 integers and print the list.
"""lst=[]
for i in range(1,11): 
    if i!=0: 
        lst.append(i)    
print(lst)

#Write a program to add an element to a list at the end.
lst=[2,4,5,6,7,3,6,2,8]
lst.append(9)
print(lst)
#Remove the third element from a list
lst.pop(2)
print(lst)
#Find the length of a given list.
print(len(lst))
#Reverse a list using slicing.
lst2='python'
print(list(lst2[::-1]))

#Create a list of numbers from 1 to 20 and extract all even numbers into a new list.
lst=[]
for i in range(1,21): 
    if i%2==0: 
        lst.append(i)
print(lst)

#Write a program to concatenate two lists.
lst1=[2,3,4,5]
lst2=['aaa','bbb','ccc','ddd']
lst3=lst1+lst2
print(lst3)

#Find the sum and average of a list of numbers.
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}, Average: {average}")

#Check if an element exists in a list.
lst=[2,4,5,'bbb','kkk',3,6]
element=2
if element in lst: 
    print('True')
else: 
    print('False')

#Sort a list without sort()

lst = [2, 3, 4, 5, 1, 6, 2, 7]
sorted_lst = sorted(lst)  
reversed_lst = sorted(lst, reverse=True)  
print(sorted_lst, reversed_lst)

#Flatten a nested list (e.g., [[1, 2], [3, 4]] -> [1, 2, 3, 4]).

lst1=[[1,2],[3,4]]
lst2=[item for sublist in lst1 for item in sublist]
print(lst2)"""

#Remove duplicates
def removeduplicates(lst):
    return list(set(lst))
print(removeduplicates([1,3,2,5,3,7,4]))

