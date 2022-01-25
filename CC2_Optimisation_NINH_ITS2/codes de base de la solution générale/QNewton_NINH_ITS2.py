# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:43:58 2021

@author: ninht
"""
import math as m
# x**4 - 5*x**3 + 9*x + 3
# 0.65-(0.75/(1+x**2))-(0.65*x*m.atan(1/x))
y1 = input(str('Veuillez entrer la foction f(x): '))
xi = float(input('Veuillez entrer un point de départ xi: '))
dx = float(input('Veuillez entrer la valeur d\'un pas d(x) = '))
eps = float(input('Veuillez entrer la valeur d\'epsilone = '))
# xi = 0.1
# dx=0.01
# eps=0.01
def trans(y,x):
    fonction =y1
    return eval(fonction)
            
def f(x):
    # return 0.65-(0.75/(1+x**2))-(0.65*x*m.atan(1/x))
    return trans(y1,x)

def f1(x):
    return (f(x+dx)-f(x-dx))/(2*dx)

def f2(x):
    return (f(x+dx)-2*f(x)+f(x-dx))/((dx)**2)
def fp(x):
    return (f(x+dx))
def fn(x):
    return(f(x-dx))


i=1 

while True :
    # xF=xi-((dx*(fp(xi)-fn(xi)))/(2*(fp(xi)-2*f(xi)+fn(xi))))
    
    xF=xi-f1(xi)/f2(xi)
    print(f'\n---------------Iteration {i}---------------')
    print(f'\nx{i+1}=',xF, f'\n|f\'(x{i+1})|=', abs(f1(xF)))
    
    if (abs(f1(xF))<eps):
        break
    else:
        xi=xF
        i=i+1
        continue 
    
print('\n------------------Solution------------------','\n')    
print(f'\nLe processus ayant convergé, nous considérons la solutionoptimale comme x* ≈ x{i+1} =',xF)