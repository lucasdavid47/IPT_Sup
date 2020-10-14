#Python
N=300
Tes = [1 for i in range(0, N+1)]
for i in range(2,int(N**(1/2))):
    for j in range(i*i, N+1, i):
        Tes[j] = 0
for i in range(1,N):
    if Tes[i]==1:
        print(i)

print("\n*********")
k=N
while Tes[k] == 0:
    k -= 1
print(k)
