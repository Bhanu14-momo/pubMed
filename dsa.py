#Reverse a String
"""def reverse_str(str):
    reverse_str=" "
    for char in str: 
        reverse_str=char + reverse_str
    return reverse_str
str=input("enter from user : ")
res=reverse_str(str)
print(res)"""

#Find the Maximum Subarray Sum (Kadane's Algorithm)
"""def max_subarr_sum(arr):
    max_sum=float('-inf') 
    curr_sum=0
    for num in arr: 
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum 
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res=max_subarr_sum(arr)
print(f'The max_subarr_sum  is: ',res)"""

#Find the duplicates
"""arr=[1, 2, 3, 4, 4, 5, 6, 7, 7]
def findupl(arr):
    res=set()
    dupl=set()
    for num in arr:
        if num in res:
            dupl.add(num)
        res.add(num)
    return list(dupl)
print(findupl(arr))"""

# Find the Largest Sum Contiguous Subarray (Kadane’s Algorithm)
"""arr= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def longcons(arr):
    max_num=0
    curr_num=0
    for num in arr:
        curr_num=max(num,curr_num+num)
        max_num=max(max_num,curr_num)
    return max_num
print(longcons(arr))"""

#substrings :
"""s='Bhanu'
def substrings(s):
    n=len(s)
    res=[]
    for i in range(n):
        for j in range(i+1,n+1):
            res.append(s[i:j])
    return res
print(substrings(s))"""

#LinkedList
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertHead(self,newNode):
        newNode.next=self.head
        self.head=newNode
    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while lastNode.next:
                lastNode=lastNode.next
            lastNode.next=newNode
    def printList(self):
        currNode=self.head
        if self.head is None:
            print("Empty LinkedList")
        while currNode:
            print(currNode.data,end='->')
            currNode=currNode.next
        print('None')
linkedlist=LinkedList()
linkedlist.insertEnd(Node(1))
linkedlist.insertEnd(Node(3))
linkedlist.insertEnd(Node(4))
linkedlist.insertEnd(Node(7))
linkedlist.insertHead(Node(0))
linkedlist.printList()



