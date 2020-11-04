import numpy as np


def f(x):
    return np.log(x)-np.cos(x)

def dicho(f, a, b, ecart):
    aa,bb= a,b
    while np.abs(bb - aa) > ecart:
        c = (aa + bb) / 2
        if f(c) < 0:
            aa = c
        elif f(c) > 0:
            bb = c
    return [aa, bb, a, b]


print(dicho(f,0.0001,np.pi/2-0.0001, 0.0001))