import random
def Randomb():
    num = random.randint(0, 1)
    return num
 
def BinaryNumber(n):
    bstr = ""

    for i in range(n):

        x = Randomb()
 
        bstr += str(x)

    print(bstr)
# def addZeros(strr, n):
#     for i in range(n):
#         strr = "0" + strr
#     return strr
 

# def getXOR(a, b):
 
    
#     aLen = len(a)
#     bLen = len(b)
 
   
#     if (aLen > bLen):
#         b = addZeros(b, aLen - bLen)
#     elif (bLen > aLen):
#         a = addZeros(a, bLen - aLen)
 
   
#     lenn = max(aLen, bLen);
 
    
#     res = ""
#     for i in range(lenn):
#         if (a[i] == b[i]):
#             res += "0"
#         else:
#             res += "1"
 
#     return res
 

N = int(input())

r = int(BinaryNumber(N))
s = int(BinaryNumber(N))


y = int(r,2) ^ int(s,2)

result = ('{0:s}'.format(y))


for i in range(result):
    count = 0
    if result[i] == 1:
        count = count + 1
    else:
        count = 0

if count % 2 == 0:
    print("TEAM 1")
else:
    print("TEAM 2")