# 203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    temp = head
    prev = head

    while(temp == None):
        if(temp.val == val):
            if(prev == head):
                head = temp.next
            if(temp.next == None):
                temp = None
                break
            prev.next = temp.next
            temp = temp.next

        temp = temp.next
                    
