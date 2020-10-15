from math import sqrt, log
from time import time, strftime

while True:
    le_max=max(2,int(eval(input("Bonjour. Entrez un entier naturel > 1"))))
    test_print = input("Sortie des premiers obtenus: console (c) - fichier (f) ?")
    t0= time()
    test_premier = [1 for k in range(0, le_max+1)]
    sqrt_max = int(sqrt(le_max))
    les_premiers = [2]
    jj = 3
    while jj <= sqrt_max:
        if test_premier[jj]:
            jj2 = jj*2
            kk = jj*jj
            while kk <= le_max:
                test_premier[kk] = 0
                kk += jj2
        jj += 2
    for ii in range(jj, le_max+1, 2):
        if test_premier[ii]:
            les_premiers.append(ii)
    t1 = time()-t0

    print("*****************************************************")
    if test_print == "c":
        print(les_premiers)
    elif test_print == "f":
        f = open("Premeirs_Eratosthene_"+str(le_max)+strftime(" (%Y-%m-%d.txt"), ('w'))
        f.write(str(les_premiers))
        f.close()
    elif isinstance(eval(test_print), int):
        print(les_premiers[-eval(test_print):])
        print("**************************************************")
        print("Il y a plus %d nombres premiers entre 2 et %d." % (len(les_premiers), le_max))
        print("De plus, on a %d. (ln(%d)-1) = %f." %(le_max,le_max,le_max/log(le_max)-1))
        print("Et le temps de calcul est de %. 4f s." %t1)
        print("**************************************************")

        if(input("Voulez-vous continuer ce petit jeu (o-n) ?") == "n") : break