# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 04:01:37 2022

@author: ninht
"""


def trans(y,x):
    fonction = y
    return eval(fonction)           
def f(x):
    return trans(y1,x)
def f1(x):
    return trans(y2,x)

if __name__ == "__main__":
    y1= 'x**3 - 7*x**2 + 8*x -3'
    y2= '3*x**2 - 14*x + 8'
    xi = 5   
    eps = 0.001
    i=1
    while True :
        xF=xi-f(xi)/f1(xi)
        print(f'\n---------------Iteration {i}---------------')    
        print(f'\nx{i+1}=',xF, f'\n|f\'(x{i+1})|=', abs(f(xF)),'\n')
           
        if (f(xF)<eps):
            break
        xi=xF
        i=i+1
    print('\n------------------Solution------------------','\n')   
    print(f'\non a |f(x{i+1})|=', f(xF), '< eps. Notre solution est donc : x* = ', xF)

