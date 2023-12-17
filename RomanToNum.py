def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    value = 0
    for i in range(len(s)):
        if(s[i] == "M"):
            if(s[i-1] == 'C' and i>0):  continue
            value += 1000

        if(s[i] == "D"):
            if(s[i-1] == 'C' and i>0):  continue
            value += 500

        if(s[i] == "C"):
            if(s[i-1] == 'X' and i>0):  continue
            if(i == len(s)-1):
                value+=100
                break
            if(s[i+1] == "M"):
                value += 900
            elif(s[i+1] == "D"):
                value += 400
            else:
                value += 100

        if(s[i] == "L"):
            if(s[i-1] == 'X' and i>0):  continue
            value += 50

        if(s[i] == "X"):
            if(s[i-1] == 'I'  and i>0):  continue
            if(i == len(s)-1):
                value+=10
                break
            if(s[i+1] == "L"):
                value += 40
            elif(s[i+1] == "C"):
                value += 90
            else:
                value+=10

        if(s[i] == "V"):
            if(s[i-1] == 'I' and i>0):  continue
            value += 5

        if(s[i] == "I"):
            if(i == len(s)-1):
                value+=1
                break
            if(s[i+1] == "V"):
                value += 4
            elif(s[i+1] == "X"):
                value += 9
            else:
                value+=1
    print(value)
    return value
    

romanToInt("MCMXCIV")
