# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:59:42 2020

@author: Carlos_Carreño
"""
#%% 1
a = int(input("ingrese el numero a: "))
c = int(input("Ingrese el numero c: "))

print("El productos de los dos numeros es " + str(a*c))
print("El doble del numero a es " + str(a*2))

#%% 2

b = int(input("Ingrese el numero b: "))
print("El cuadrado del numero b es " + str(b**2))

d = int(input("Ingrese el numero d: "))
print("La raiz cuadrado del numero d es " + str(d**1/2))

#%% 3
a = int(input("ingrese el numero a que acompaña a X ala dos: "))
b = int(input("ingrese el numero b que acompaña a X : "))
c = int(input("Ingrese el numero c: "))
d = (b**2)-(4*a*c)
if d>0 :
    x1=(-b+(d**1/2))/2*a
    x2=(-b-(d**1/2))/2*a
    print("x1 es igua a :" + str(x1))
    print("x2 es igua a :" + str(x21))
elif d == 0 :
    print("x1 y x2 son iguales")
    print((-b/2*a))
elif d<0 :
    print("no existe solucion")

