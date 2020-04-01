# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:49:59 2020

@author: CarlosCJ
"""
import numpy as np

kellos = np.array([27834,23789,30189,30967,32501,32701+31665,17155,4614,834])

# Punto 1
def promedio(r,t):
    c = 0
    n = 1
    for p in range(r,t):
        c = c + kellos[p]
        n += 1
    prome = c /n
    return prome
def compa(a1,b1,a2,b2):
    prome1 = promedio(a1,b1)
    prome2 = promedio(a2,b2)
    dif = prome1 - prome2
    return dif
print("La diferencia es de " + str(compa(0,1,8,9)))
# punto 2
def menorr(kellos):
    menor = kellos[0]
    long = len(kellos)
    for i in range(1,long):
        if menor > (kellos[i]) :
            menor = kellos[i]
    return menor
def mayorp(kellos):
    mayor = kellos[0]
    long = len(kellos)
    for r in range(1,long):
        if mayor < kellos[r]:
            mayor = kellos[r]
    return mayor
mayor = mayorp(kellos)
menor = menorr(kellos)
def dife(mayor,menor) :
    Dif = mayor - menor
    return Dif
print("la diferencia entre la utilidad del año de mayor y la de menor es " +str(dife(mayor,menor)))
# Punto3
def mediana(kellos):
    keo = np.sort(kellos)
    m = int(len(keo))
    if (m%2) == 0 :
        m = (m/2)-1
        p1 = keo[int(m)]
        p2 = keo[int(m+1)]
        medianaa = (p1 + p2)/2
    else :
        m =(m//2)+1
        medianaa = keo[int(m)]
    return medianaa
print("La mediana es " + str(mediana(kellos)))
# Punto 4
def compMandM(promedio,mediana):
    media = promedio(0,9)
    medianaa = mediana(kellos)
    print("La media es " + str(media))
    print("la mediana es " + str(medianaa))
    if media < medianaa :
        M = medianaa - media
        print("Es mayor la mediana con " + str(M))
    else :
        M = media - mediana
        print("la media es mas grande por " + str(M))
print(compMandM(promedio, mediana))
# punto 5
def Porce(kellos):
    c = 0
    long = len(kellos)
    p = 2008
    for r in range(0,long):
        c = c + kellos[r]
    for m in range(0,long) :
        porap = ((kellos[m])*100)/c
        print("le porcentaje que aporta el año " + str(p) + " es " + str(porap) + "%")
        p = int(p) + 1 
print(Porce(kellos))
# punto 6
def deficit(kellos) :
    long = len(kellos)
    D2017 = kellos[long-1]
    D2016 = kellos[long-2]
    deficits = D2016-D2017
    print("El deficit del 2017 comparado con el de el 2016 es de " + str(deficits) + " cop")
print(deficit(kellos))
# putno 7
def defiporcentaje(kellos) :
    long = len(kellos)
    A = 2017
    for i in range(0, long-1):
        ult = kellos[long-1]
        defi = kellos[long-2] - ult
        defiporce = (defi*100)/ult
        long = long-1
        print("el deficit en porcenta del año " + str(A) + " es "  + str(round(defiporce,2)) + " %")
        A = A - 1
print(defiporcentaje(kellos))
