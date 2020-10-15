import numpy
N= 100
n=1
Resultat=1
while(n<N):
    Resultat *= n
    n += 1
print(Resultat)


y=100
x=1
while(x+numpy.log(x) <= y):
    x += 0.1
x -= 0.1
print([x, x+numpy.log(x)])

