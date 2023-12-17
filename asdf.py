# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = ListNode(None)
        head = l
        while True:
            if(list1 == None):
                l.next = list2
                break
            if(list2 == None):
                l.next = list1
                break
            if(list1.val >= list2.val):
                l.next = list2
                list2 = list2.next
            else:
                l.next = list1
                list1 = list1.next
            l = l.next
        
        return head.next