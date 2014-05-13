import numpy as np
def trapz(func,a,b,N):   
    func = lambda x: x**4 - 2*x + 1
    h = (b-a)/N
    k = np.arange(1,N)
    It = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    return It

def simps(func,a,b,N):
    func = lambda x: x**4 - 2*x + 1
    h = (b-a)/N
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    Is = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    return Is