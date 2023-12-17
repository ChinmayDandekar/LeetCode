# 1328. Break a Palindrome

def breakPalindrome(palindrome):
    """
    :type palindrome: str
    :rtype: str
    """
    for i in palindrome:
        if(ord(i) > 97):      
            return palindrome.replace(i,chr(ord(i)-1),1)
        
    for i in palindrome:
        return palindrome.reversed().replace(i,chr(ord(i)+1),1)
    return palindrome

print(breakPalindrome("aba"))