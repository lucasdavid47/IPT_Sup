import numpy as np

def f(x):
    return x - np.cos(x)


a=0
b= np.pi/2

while np.abs(b - a) > 1/1000:
    c = (a + b) / 2
    if f(c) < 0:
        a = c
    elif f(c) > 0:
        b = c


print(a, b)


