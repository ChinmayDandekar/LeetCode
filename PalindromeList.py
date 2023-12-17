
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    print(head)
    reverseHead = head.reverse()
    print(reverseHead)
    for i in range(len(head)):
        if head[i] != reverseHead[i]:
            return False
    return True    
    


i = isPalindrome([1,2,2,1])
print(i)