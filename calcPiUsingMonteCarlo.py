# circle area = pi * r^2
# square = 2*2 = 4  if r = 1 
# c area = 3.14
# equation of the circle ==> x^2 + y^2 <= 1
# so , we will put many simple points 

import numpy as np
import random as rn

x = []
y = []

def calcPi(n):
    counter = 0 
    for k in range(1 , n+2):
        x.append(rn.random())
        y.append(rn.random())
        
    for gg in range(1 , n+1):
        for jj in range(1 , n+1):
            if ((x[gg]**2) + ((y[jj])**2) <= 1 ):
                counter += 1
    
    pii = (float(counter)) / (n**2)
    return pii

calculatedPi = 4*calcPi(3000)

print('calculated pi = ' + str(calculatedPi))
print('difference = ' + str(np.pi - calculatedPi))    