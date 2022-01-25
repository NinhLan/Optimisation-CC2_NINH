# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 04:01:37 2022

@author: ninht
"""

# x**4 - 5*x**3 + 9*x + 3
# 4*x**3-15*x**2+9
# x**3 - 7*x**2 + 8*x -3
# 3*x**2 - 14*x + 8



# a=4
# b=6
# xi=int((a+b)/2)
# eps=0.001

def trans(y,x):
    fonction = y
    return eval(fonction)           
def f(x):
    return trans(y1,x)
def f1(x):
    return trans(y2,x)

if __name__ == "__main__":
    y1= input(str('Veuillez entrer la foction f(x): '))
    y2= input(str('Veuillez entrer la foction dérive f\'(x): '))
    c = input('Vous voulez entrer un intervalle [a,b] (taper 1) ou un point de départ xi (taper 2)? :')
    if c=='1' :
        a=int(input('Veuillez entrer le 1er valeur d\'intervalle: '))
        b=int(input('Veuillez entrer le 2ème valeur d\'intervalle: '))
        xi=int((a+b)/2)
    if c=='2':
        xi = float(input('Veuillez entrer un point de départ xi: '))
        
    eps = float(input('Veuillez entrer la valeur d\'epsilone = '))
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

