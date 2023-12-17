def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counter = len(nums)
    i = 0
    while (True):
        if(i == counter-1):
            break
        if(nums[i] == nums[i+1]):
            nums.append(nums.pop(i))
            counter-=1
        else:
            i+=1
        
    return counter