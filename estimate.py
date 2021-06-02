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

wallis(10000)
monte_carlo(1222)
