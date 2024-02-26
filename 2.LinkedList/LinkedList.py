"""
REMEBER BIG(O) Depends on Operations        
O(1) for adding at the either ends of the list
O(n) for adding some items at the end of list
O(1) for removing at the start of the node
O(n) for adding/removing element in between the list
"""
#To Create a Node
class Node:
    #Node  Constructor
    def __init__(self, value):
        self.value =  value
        self.next =  None


    

class LinkedList:
    #To Create a New Linked List
    def __init__(self, value):
        new_node =  Node(value)
        self.head =  new_node
        self.tail =  new_node
        self.length = 1
    
    #To Print the List
    def print_list(self):
        temp =  self.head
        while temp is not None:
            print(temp.value)
            temp =  temp.next

    # #To add new node at end   
    def append(self,value):
        new_Node =  Node(value)
        if self.head  is None:
            self.head =  new_Node
            self.tail = new_Node
        else:
            self.tail.next =  new_Node
            self.tail =  new_Node
        self.length += 1
        return True
     
    
    # #To remove a node from the end    
    def Pop(self):
        if self.length == 0:
            return None
        temp =  self.head
        pre =  self.head
        while temp.next is not None:
            pre =  temp
            temp =  temp.next
        self.tail =  pre
        self.tail.next =  None
        self.length -= 1
        #If final Lenght to 0
        if self.length == 0:
            self.head = None
            self.tail =  None
        return temp.value


    # #To Insert New node into the List   
    def prepend(self, value):
        new_node =  Node(value)
        if self.length == 0:
            self.head =  new_node
            self.tail  = new_node
        else:
            new_node.next = self.head
            self.head =  new_node
        self.length += 1
        return True
    #Remove the First Element
    def PopFirst(self,value):
        new_node =  Node(value)
        if self.length == 0:
            None
        else:
            temp =  self.head
            self.head =  self.head.next
            temp.next = None
            self.length -= 1
            if self.length == 0:
                self.tail =  None 
        return temp.value


    
myLinkedList =  LinkedList(4)

myLinkedList.append(5)
myLinkedList.append(6)
myLinkedList.prepend(7)
myLinkedList.Pop()
print(f"Linked List after poping: \n",LinkedList.print_list(myLinkedList))
