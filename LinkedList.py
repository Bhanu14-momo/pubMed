#create Node
#create Linkedlist
#Append node
#print Node

# 1]create a basic linkedlist to display data
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if not self.head:
            self.head=newNode
        else:
            lastNode=self.head
            while  lastNode.next:
                lastNode=lastNode.next
            lastNode.next=newNode
    def printList(self):
        currentNode=self.head
        if self.head  is None:
            print("Linked List is Empty.")
            return
        while currentNode:
            print(currentNode.data,end="->")
            currentNode=currentNode.next
        print("None")
linkedlist=LinkedList()
linkedlist.insert(Node(1))
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(7))
linkedlist.printList()"""


# 2]insert Node at head postion i.e beggining:
"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insertEnd(self,newNode):          #insert at End
        if not self.head:
            self.head=newNode
        else:
            lastNode=self.head
            while  lastNode.next:
                lastNode=lastNode.next
            lastNode.next=newNode
    def insertHead(self,newNode):       #insert at Head
        newNode.next=self.head
        self.head=newNode
    def printList(self):
        currentNode=self.head
        if self.head  is None:
            print("Linked List is Empty.")
            return
        while currentNode:
            print(currentNode.data,end="->")
            currentNode=currentNode.next
        print("None")
linkedlist=LinkedList()
linkedlist.insertEnd(Node(1))
linkedlist.insertEnd(Node(3))
linkedlist.insertEnd(Node(4))
linkedlist.insertEnd(Node(7))
linkedlist.insertHead(Node(8))
linkedlist.printList()"""


#insert the node at spefic position:
"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if not self.head:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAt(self,newNode,position):
        if position==0:
            newNode.next=self.head
            self.head=newNode
            return
        currentNode=self.head
        currentPosition=0
        while currentNode is not None and currentPosition<position-1:
            currentNode=currentNode.next
            currentPosition+=1
        if not currentNode:
                print("EmptyNode")
                self.insert(newNode)
        else:
            newNode.next=currentNode.next
            currentNode.next=newNode
    def printList(self):
        currentNode = self.head
        if self.head is None:
            print("Linked List is Empty.")
            return
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

# Create LinkedList
linkedlist = LinkedList()

# Insert at end
linkedlist.insert(Node(1))
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(7))

# Insert at specific positions
linkedlist.insertAt(Node(0), 0)  # Insert at head
linkedlist.insertAt(Node(2), 2)  # Insert at position 2

# Print list
linkedlist.printList()"""


# 3] kthelement of linkelist:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,newNode):
        if not self.head:
            self.head=newNode
        else:
            lastNode=self.head
            while  lastNode.next:
                lastNode=lastNode.next
            lastNode.next=newNode
    def kthElement(self,k):
        curr=self.head
        for _ in range(k-1):
            if curr:
                curr=curr.next
        return curr.data if curr else -1

    def printList(self):
        currentNode=self.head
        if self.head  is None:
            print("Linked List is Empty.")
            return
        while currentNode:
            print(currentNode.data,end="->")
            currentNode=currentNode.next
        print("None")
linkedlist=LinkedList()
linkedlist.insert(Node(1))
linkedlist.insert(Node(3))
linkedlist.insert(Node(4))
linkedlist.insert(Node(7))
k=2
print(f'linked list of kthelement of {k} is {linkedlist.kthElement(k)}')
