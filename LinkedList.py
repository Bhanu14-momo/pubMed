#insert node
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is  None:
            self.head=new_node
            print(f'{data} inserted as head.')
            return
        last=self.head
        while  last.next:
            last=last.next
        last.next=new_node
        print(f'{data}')
    def display(self):
        if self.head is None:
            print("LL is Empty.")
            return
        curr=self.head
        while curr:
            print(curr.data,end='->')
            curr=curr.next
        print('None')
LL=SLL()
LL.insert(10)
LL.insert(20)
LL.insert(30)
LL.insert(40)
LL.display()"""

#create a linkedlist

"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class create:
    def __init__(self):
        self.head=None
    def node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            last=self.head
            while last.next is not None:
                last=last.next
            last.next=new_node
    def printll(self):
        if self.head is None:
            print("LL is empty")
        else:
            curr=self.head
            while curr:
                print(curr.data,end='->')
                curr=curr.next
            print('None')
l1=create()
l1.node(1)
l1.node(2)
l1.node(3)
l1.printll() """

#reverse linkedlist usinf iterative

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class reverse:
#     def __init__(self):
#         self.head=None
#     def insert(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node   
#         else:
#             last=self.head
#             while last.next is not None:
#                 last=last.next
#             last.next=new_node
#     def reverseList(self):
#         prev,curr=None,self.head
#         while curr:
#            next=curr.next
#            curr.next=prev
#            prev=curr
#            curr=next
#         self.head=prev
#     def printlist(self):
#         curr=self.head
#         while curr:
#             print(curr.data,end='->')
#             curr=curr.next
#         print("None")

# L=reverse()
# L.insert(10)
# L.insert(20)
# L.insert(30)
# print("original LL:")
# L.printlist()
# L.reverseList()
# print("reversed LL:")
# L.printlist()


# insert at start:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
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
        if self .head is None:
            print("LL is Empty")
            return
        curr=self.head
        while curr:
            print(curr.data,end='->')
            curr=curr.next
        print('None')
n1=Node('John')
n2=Node('Ben')
n3=Node('Mattew')
L=LL()
L.insertEnd(n1)
L.insertEnd(n2)
L.insertHead(n3)
L.printList()




        