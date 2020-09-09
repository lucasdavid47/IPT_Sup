"""DAVID Lucas
   CYR V, MPSI-S
   09/09/2020"""

"""
Rappels boucle
"""
for k in range(5, 20):
    print(k)
    print(k * k)

"""
Print en dehors de la boucle, 1 seul print
"""

L = []
for k in range(0, 101):
    L.append(k * k)
print(L)

"""
Avec print dans la boucle, 100 print
"""

P = []
for k in range(0, 101):
    P.append(k * k)
    print(P)

"""Somme liste, en utilisant range"""
PrimeNumbers = [2, 3, 5, 7, 11, 13, 17, 19]
print(len(PrimeNumbers))
print(PrimeNumbers[5])
Sum = 0
for k in range(0, len(PrimeNumbers)):
    Sum = Sum + PrimeNumbers[k]
print(Sum)

"""Somme sans range, Parcourir la liste"""
T = 0
for toto in PrimeNumbers:
    T = T + toto
print(T)


"""Somme sans range, parcourir liste utilisation R+. 
   Forme optimale"""
R = 0
for k in PrimeNumbers:
    R += k
print(R)

"""Produit de Prime numbers"""
product= 1
for p in PrimeNumbers:
    product *= p
print(product)

"""Concatène les deux listes"""
L2=[1,2,3,4,5,6,7,8]
print(L + L2)
