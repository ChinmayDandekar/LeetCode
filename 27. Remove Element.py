def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0 
    counter = len(nums)
    while(True):
        if(i == counter):
            break
        if(nums[i] == val):
            nums.append(nums.pop(i))
            counter-=1
        else:
            i+=1
    return counter