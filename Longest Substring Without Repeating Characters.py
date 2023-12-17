# Longest Substring Without Repeating Characters


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxc = 0
    c = 0
    lst = []

    for i in range(len(s)):
        while(True):
            if(i+c >= len(s)):
                if(c>maxc):
                    maxc = c
                break
            # print(s[i+c], c, lst  )
            if(s[i+c] in lst):
                if(c > maxc):
                    maxc = c
                c = 0
                lst = []
                break
            else:

                lst.append(s[i+c])
                c += 1     
        # print('\n')  
    print(maxc)
    return maxc

lengthOfLongestSubstring("abcabcbb")
lengthOfLongestSubstring("pwwkew")
lengthOfLongestSubstring("bbbb")
lengthOfLongestSubstring("dvdf")





