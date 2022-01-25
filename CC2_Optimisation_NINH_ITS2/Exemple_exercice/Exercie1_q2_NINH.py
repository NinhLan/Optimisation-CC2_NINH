# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 05:14:10 2022

@author: ninht
"""

def trans(y,i,s,x1):
    fonction= y1
    return eval(fonction)
def f(i,s,x1):
    return trans(y1,i,s,x1)

# def f(i,s):
#     return x(i,s)**2 - 1.5 * x(i,s)

def x(i,s,x1):
    if i > 0:
        return x1 + (i - 1) * s
    else:
        return x1 + (i + 1) * s

def pasVA(i,s):
    
    if f(2,s,x1) < f(1,s,x1) :
        while f(i+1,s, x1) < f(i,s,x1): 
            i+=1
            s=2*s
            xa = x(i-1,s,x1)
            
            print (f'x{i} =',xa)
            
    if f(2,s,x1) > f(1,s,x1):
        while f(i+1,s,x1) > f(i,s,x1):
            s=2*s
            xa = x(i-1,s,x1)
            print (f'x{i} =',xa)
            i-=1
    elif f(2,s,x1) == f(1,s,x1):
        xa = x(1,s,x1)
        print (f'x{i} =',xa)
    elif f(2,s,x1) > f(1,s,x1) and f(-2,s,x1) > f(1,s,x1):
        xa = x(-2,s,x1)
        print (f'x{i} =',xa)
    return ('Le point x* ≈ ' +str(xa)+' est l\'optimum ')
if __name__ == "__main__":

    y1 = 'x(i,s,x1)**5 - 5*x(i,s,x1)**3 -20*x(i,s,x1) +5'
    x1 = 0.0
    s = 0.05
    i = 1
    r=pasVA(i,s)
    print(r)
    
    