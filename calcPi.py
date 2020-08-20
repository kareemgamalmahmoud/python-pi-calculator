# pi = sqrt(12)(1 - (1/3.3^1) + (1/5.3^2) - (1/7.3^3) + ...) 

import math 

pi = 0 

for k in range(20):
    pi += pow(-3 , -k) / (2*k + 1)

pi *= math.sqrt(12)

print('pi = ' , pi)


# to get Error rate
print('error = ' , abs(pi-math.pi))    

# that mean when i increase the num of the range the error will be decrease