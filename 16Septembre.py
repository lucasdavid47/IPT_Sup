L1=[1,2,3,4]
L2=[9,7,5,3]
L=[]
n = len(L1)

for k in range(0,n):
    L.append(L1[k] +L2[k])

A=[[1,2,3], [4,5,6], [7,8,9]]
B=[[4, 3, 2], [1, 2, 3], [0,1,0]]
L=[[],[], []]

C=[]
for i in range(0, 3):
    L=[]
    for j in range(0, 3):
        L.append(A[i][j] + B[i][j])
    C.append(L)
print(C)

D=[]
for i in range(0, 3):
    L=[]
    for j in range(0,3):
        S=0
        for k in range(0, 3):
            S += A[i][k]*B[k][j]
        L.append(S)
    D.append(L)

for x in D:
    print(x)
