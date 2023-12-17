# Longest Palindromic Substring


def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        maxs = ""
        slen = len(s)
        for i in range(slen):
            c = 0
            ss = ""
            while(True):
                if(i + c == slen):
                    break
                ss += s[i+c]
                if( len(ss) > len(maxs)):
                    if(ss == ss[::-1]):
                        maxs = ss
                c+=1
        return maxs