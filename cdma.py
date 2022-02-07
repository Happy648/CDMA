Ad=int(input("Enter Sender A's data:"))
Bd=int(input("Enter Sender B's data:"))

if Ad==0:
    Ad=-1
if Bd==0:
    Bd=-1

codeA=[int(item) for item in input("Enter A's PN sequence: ").split()]
codeB=[int(item) for item in input("Enter B's PN sequence: ").split()]

for i in range(len(codeA)):
    if codeA[i]==0:
        codeA[i]=-1

for i in range(len(codeB)):
    if codeB[i]==0:
        codeB[i]=-1

As=[Ad*i for i in codeA]
Bs=[Bd*i for i in codeB]

Cs=[As[i]+Bs[i] for i in range(len(As))]

ResultA=[Cs[i]*codeA[i] for i in range(len(codeA))]
ResultB=[Cs[i]*codeB[i] for i in range(len(codeB))]

sumA=sum(ResultA)
sumB=sum(ResultB)

if sumA>0:
    print("A's transmitted data is 1")
else:
    print("A's transmitted data is 0")

if sumB>0:
    print("B's transmitted data is 1")
else:
    print("B's transmitted data is 0")


