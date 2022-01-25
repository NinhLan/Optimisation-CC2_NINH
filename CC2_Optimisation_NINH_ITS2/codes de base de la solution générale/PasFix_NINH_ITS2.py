# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 01:31:58 2021

@author: ninht
"""

def trans(y,i):
    fonction= y1
    return eval(fonction)
def f(i):
    return trans(y1,i)
# def f(i):
#     return x(i)**2 - 1.5 * x(i)

def x(i):
    if i>0:
        return x1 + (i - 1) * s
    else:
        return x1 - (i - 1) * s

def pasfixe(i):
    if f(2) < f(1) :
        while f(i + 1) < f(i): 
            i+=1
            xa = x(i)
            xb = x(i-1)
            print (f'x{i} =',xa)
    if f(2) > f(1):
        while f(i + 1) > f(i):
            i-=1
            print (f'x{i} =',xa)
    elif f(2) == f(1):
        xa = x(1)
        xb = x(2)
        print (f'x{i} =',xa)
    elif f(2) > f(1) and f(-2) > f(1):
        xa = x(-2)
        xb = x(2)
        print (f'x{i} =',xa)

    return i,xa,xb

# x1 = 0.0
# s = 0.05

if __name__ == "__main__": 
    y1 = str(input('Veuillez entrer la foction f(x): '))
    x1 = float(input('Veuillez entrer un point de départ x1: '))
    s = float(input('Veuillez entrer la valeur d\'un pas s: '))
    # x1 = 0.0
    # s = 0.05
    i = 1
    r=pasfixe(i)   
    print("Point minimum x* = ",r[1],"\nf(x*)=",f(r[0]))
             

    