import unittest
import math
import random

import random
import math

def wallis(n):
    l=[]
    final_product=1
    for i in range(n):
        l.append(4*((i+1)**2)/(4*((i+1)**2)-1))
    for i in range(n):
        final_product = final_product * l[i]
    print(final_product*2)    
    return(final_product*2)






def monte_carlo(n):
    incir=0
    insqr=0
    for i in range(n):
        x=random.random()
        y=random.random()
        z=math.sqrt((float(x)**2)+(float(y)**2))
        if z<=1.0:
            incir=incir+1
        else:
            insqr=insqr+1
    print(incir*4*4/(incir*4+insqr*4))
    return (incir*4*4/(incir*4+insqr*4))




class TestWallis(unittest.TestCase):

def test_low_iters(self):

for i in range(0, 5):

pi = wallis(i)

self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")

def test_high_iters(self):

for i in range(500, 600):

pi = wallis(i)

self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

class TestMC(unittest.TestCase):

def test_randomness(self):

pi0 = monte_carlo(15000)

pi1 = monte_carlo(15000)

self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

def test_accuracy(self):

for i in range(500, 600):

pi = monte_carlo(i)

self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

if __name__ == "__main__":

unittest.main()

from random import random

radius = 2
