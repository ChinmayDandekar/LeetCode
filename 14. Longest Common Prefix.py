

# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """

#     j = 0
#     for i in range(len(strs)-1):
#         while(True):
#             print(i ,j, strs[i][j])
#             if(len(strs[i][j])<j):
#                 return strs[0][0:j]
#             if(strs[i][j] == strs[i+1][j]):
#                 j+=1
#             else:
#                 return strs[0][0:j]
        
#     return strs[0][0:j]


# print(longestCommonPrefix(["flower","flow","flight"]))
            




            
def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        counter = -1
        for j in range(len(strs[0]-1)):
            if j > strs[0]
            if (strs[i][j] != strs[i+1][j] ):
                return ""
            