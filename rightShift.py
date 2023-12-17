


def main():
    a = int(input())
    b = int(input())
    maxCounter = 0
    maxValue = 0
    for i in range(len(str('{0:b}'.format(b)))):
        val = a ^ b
        print(i,a,b,val)
        if(val> maxValue):
            maxValue = val
            maxCounter = i
        b = b>>1
        print(b)
    print(maxCounter,maxValue)
    return maxCounter,maxValue   
    

main()