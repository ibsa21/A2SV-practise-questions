class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):

    def __init__(self):
        self.root = None
        self.counter = 0

    def get(self, index):
        if index < 0 or index >= self.counter:
            return -1
        
        tempNode = self.root
        for _ in range(index):            
            tempNode = tempNode.next

        return tempNode.val
    
    def addAtHead(self, val):
        newNode = ListNode(val)
        if self.root==None:
            self.root = newNode
            self.last = newNode
        else:
            temp = self.root
            newNode.next = self.root
            self.root = newNode
        self.counter +=1 

    def addAtTail(self, val):
        self.addAtIndex(self.counter, val)
        

    def addAtIndex(self, index, val):
        if index > self.counter:
            return
        
        tempNode = self.root
        newNode = ListNode(val)
                
        if index <= 0:
            newNode.next = tempNode
            self.root = newNode
        else:                        
            for i in range(index - 1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            tempNode.next = newNode    
            
        self.counter += 1
        
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.counter:
            return
        
        tempNode = self.root
        
        if index == 0:
            self.root = self.root.next
        else:
            for i in range(0, index - 1):
                tempNode = tempNode.next
            tempNode.next = tempNode.next.next              

        self.counter -= 1
