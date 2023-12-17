# 12. Integer to Roman

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    dic = {
        0:["X","V","I"],
        1:["C","L","X"],
        2:["M","D","C"],
        3:["","","M"]
    }
    c = 0
    result=''
    while num > 0:
        i = num%10
        num = int(num/10)
        if(i<4):
            for j in range(i):
                result = dic[c][2] + result
        elif(i == 4):
            result = dic[c][2] + dic[c][1] + result
        elif(i >= 5 and i<9):
            for j in range(i-5):
                result = dic[c][2] + result
            result = dic[c][1] + result
        elif(i == 9):
            result = dic[c][2] + dic[c][0] + result
        if(c<3):
            c += 1
    print(result)


intToRoman(1994)