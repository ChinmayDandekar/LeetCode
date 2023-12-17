
def checkLen(n):
    while True:
        if(len(str(n))==1):
            break
        t = 0
        for i in str(n):
            t += int(i)
        n = t
        return n

def main():
    name = input()
    dob = input()
    char = input()
    vowels = ['a','e','i','o','u']

    x = 0
    for n in name:
        if n in vowels:
            x += 1
    y = 0
    for i in dob:
        y += int(i)
    
    z = 0
    for a in char.lower():
        z += (ord(a)-96)
    
    checkLen(x)
    checkLen(y)
    checkLen(z)
    print(str(x)+str(y)+str(z))
    if (x == y and y==z):
        print("1")
    else:
        print("0")

main()
# results("Robinhood","1989","N")

# Input
# Sam
# 1000
# a

# Output
# 111
# 1