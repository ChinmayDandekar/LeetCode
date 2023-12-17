# 20. Valid Parentheses

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    dic = {
            '{':"}",
            "(":")",
            "[":"]"
    }

    stack = []
    for i in s:
        if i in dic:
            stack.append(i)
        else:
            if(len(stack)):
                if(dic[stack[-1]] == i):
                    stack.pop()
                else:
                    return False
            else:
                return False
        print(stack)
    if len(stack) >0:
        return False
    else:
        return True
    
print(isValid("({})"))
print(isValid("([{]})"))
 
    