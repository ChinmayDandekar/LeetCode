# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        L1 = ""
        L2 = ""
        while(True):
            if (l1 == None and l2 == None):
                break
            if (l1 != None):
                L1 = L1 + str(l1.val)
                l1 = l1.next
            if (l2 != None):
                L2 = L2+ str(l2.val)
                l2 = l2.next    
        L3 = int((L1)[::-1]) + int((L2)[::-1])         
        print(L1, L2, L3)   
        l3 = None
        for i in iter(str(L3)):
            l3 = ListNode(val=i, next= l3)   
        return l3