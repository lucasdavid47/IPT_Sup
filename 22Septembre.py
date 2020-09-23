#Somme

A=[]
B=[]
n =len(A) #nombre de lignes de A
C=[]
for i in range(0, n):
    L=[]
    for j in range(0, n):
        L.append(A[i][j]+B[i][j])
    C.append(L)

for x in C:
    print(x) #affichage ligne par ligne de C


#Produit

n = len(A)
D=[]
for i in range(0, n):
    L=[]
    for j in range(0, n):
        S=0
        for k in range(0,n):
            S += A[i][k]*B[k][j]
        L.append(S)
    D.append(L)

for x in D:
    print(x)


#Python
L=[1,2,3,4,5,6]
for k in range(0, len(L)):
    if(L[k]>3):
        L[k] *=2
    else:
        L[k] *=3
print[L]