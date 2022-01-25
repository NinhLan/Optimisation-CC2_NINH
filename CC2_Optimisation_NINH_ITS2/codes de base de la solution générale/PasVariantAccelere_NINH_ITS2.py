# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 02:44:11 2021

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
    
    # s = 0.05
    
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
    return xa
if __name__ == "__main__":
    # x1=0.0
    y1 = str(input('Veuillez entrer la foction f(x): '))
    x1 = float(input('Veuillez entrer un point de départ x1: '))
    s = float(input('Veuillez entrer la valeur d\'un pas s: '))
    i = 1
    r=pasVA(i,s)
    print("Le point x* ≈ ",r[0]," est l\'optimum ")

