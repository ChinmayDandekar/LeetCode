


# def convert(s, numRows):
#     """
#     :type s: str
#     :type numRows: int
#     :rtype: str
#     """
#     dic = []
#     for i in range(numRows):
#         c = 0
#         temp = ""
#         while(c<=len(s)):
#             temp += s[c]
#             c += ((numRows-1)*2)
       
#         print(temp, s)

def convertt(s, numRows):
    dic = {}
    c = 1
    for i in range(len(s)):
        if (c in dic):
            dic[c] = dic[c] + s[i]
        else:
            dic[c] = s[i]
        if (c == numRows):
            invert = False
        if(c == 1):
            invert = True
        if(invert):
            c+=1
        else:
            c-=1
    result = ""
    # print(dic.val)
    for val in dic.values():
        result += val
    
    print(result)
    return result



convertt("PAYPALISHIRING", 3)