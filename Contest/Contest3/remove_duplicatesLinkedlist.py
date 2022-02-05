#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    
    if not llist:
        return False

    curr_pointer = llist
    
    while curr_pointer.next:
        
        if curr_pointer.data == curr_pointer.next.data:
            newNode = curr_pointer.next.next
            curr_pointer.next = newNode
        else:
            curr_pointer = curr_pointer.next
        
    return llist;
            
        
        
        
        
    
    
    
    
    
