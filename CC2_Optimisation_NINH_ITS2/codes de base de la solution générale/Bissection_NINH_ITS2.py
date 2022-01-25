# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 01:31:58 2021

@author: ninht
"""

def trans(y,x):
    fonction = y
    return eval(fonction)
def x(n,a,b):
    if n==0 :
        return ((b-a)/2)+a
    elif n==1 :    
        return ((b-a)*(1/4))+a
    elif n==2 :    
        return ((b-a)*(3/4))+a

def f(x):
    return trans(y,x)


def bissection(a,b,valeurE):
    n=0
    i=0
    L0=b-a
    print (f'L0 = {[a,b]}')
    while ((1/2)**((n-1)/2))*L0>=(L0*valeurE*2):
        n+=1
    while i<=n:
        if f(x(2,a,b))>f(x(0,a,b)) and f(x(0,a,b))>f(x(1,a,b)):
            b= x(0,a,b)
            print('\na = ', a,', b = ', b,', x0 =', x(0,a,b))
        elif f(x(2,a,b))<f(x(0,a,b)) and f(x(0,a,b))<f(x(1,a,b)):
            a= x(0,a,b)
            print('\na = ', a,', b = ', b,', x0 =', x(0,a,b))
        elif f(x(0,a,b))<f(x(1,a,b)) and f(x(2,a,b))>f(x(0,a,b)):
            a1= x(1,a,b)
            b= x(2,a,b)
            a= a1
            print('\na = ', a,', b = ', b,', x0 =', x(0,a,b))
        i+=1
        print (f'L{i} = {[a,b]}')
        xf=a+((b-a)/2)
    return xf, f(xf), i
if __name__ == "__main__":
    y = str(input('Veuillez entrer la foction f(x): '))
    valeurE = float(input('Veuillez entrer la valeur  près de la valeur exacte, valeurE= '))
    a=int(input('Veuillez entrer le 1er valeur d\'intervalle: '))
    b=int(input('Veuillez entrer le 2ème valeur d\'intervalle: '))
    # a=0
    # b=1
    # valeurE=0.1
    b=bissection(a, b, valeurE)
    print('\n------------------Solution------------------','\n')
    print(f'En prenant le point médian de cet intervalle (L{b[2]}) commeoptimal, on obtient :')
    print('x*= ', b[0], 'et f(x*)= ', b[1])