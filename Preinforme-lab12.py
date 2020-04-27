# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:31:03 2020

@author: Carlos
"""
presion = [111.06,107.89,108.45,108.49,
           109.03,110.11,109.87,119.38,119.35,
           116.34,117.73,120.01,118.19,119.53,117.09,
           118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,
           109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,
           107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,
           121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42,
           110.67,107.73,105.76,107.85]
def mayor(a):
    k = a[0]
    c = 0
    for p in range(1,52):
        if a[p] > k:
            k = a[p]
            c = p
    return c
def menor(a):
    k = a[0]
    c = 0
    for p in range(1,52):
        r = a[p]
        if r < k : 
            k = a[p]
            c = p
    return c
def promedio(a):
    p = len(a)
    c = 0
    for t in range(0,p):
        c = c + a[t]
    pr = c/p
    return pr

def mediana(f,presion):
    p = f/2
    r = p//1
    if p == r :
        r = int(r)
        c = presion[r-1]
        return c
    else :
        c = [presion[r-1],presion[r]]
        return c
def enicima_deajo(a,b):
    d = []
    e = []
    dd = 0
    ee = 0
    for t in range(0,52):
        f = a[t]
        if f != b :
            if f > b :
                e.append(f)
                ee = ee + 1
            else:
                d.append(f)
                dd = dd + 1
    return ee,e,dd,d
def temp(presion):
    tem = []
    for p in range(0,52):
        p = presion[p]
        v = 510
        m = 17.16
        n = (82*(10**-3))
        tm = (p*v)/(m*n)
        tem.append(tm)
    return tem
def deficit(a) :
    i =promedio(a)
    g = len(a)
    c = 0
    for o in range(0,52):
        m = ((a[o])+i)**2
        c = c + m
    g = (c/g)**1/2
    return g

# -------------------------activacion-----------------------------
Me = menor(presion)
Ma = mayor(presion)
di = presion[Ma]-presion[Me]
media = promedio(presion)
f = len(presion)
mediana = mediana(f,presion)
ne, LisNE, nd, LisND = enicima_deajo(presion,media)
Temp = temp(presion)
Tempr =promedio(Temp)
Te,LisTE,Td,LisTD = enicima_deajo(Temp,Tempr)
de = deficit(Temp)

print("La diferencia entra la mayor presion y la menor presion es " + str(di))
print("la media es " + str(media))
print("la mediana es " + str(mediana))
if media != mediana :
    print("son diferentes la media y mediana")
else :
    print("son iguales la media y la mediana")
print("La nueva lista que contiene los de por encima tendria "+ str(ne) + " y serian :")
print(LisNE)
print("La nueva lista que contiene los de por debajo tendria "+ str(nd) + " y serian :")
print(LisND)
print("la tempertura promedio semanal :")
print(Temp)
print("El promedio de tempera Anual es " + str(Tempr))
print("El deficis de la temperatura es "+ str(de))
print("La nueva lista que contiene las temperaturas por encima tendria "+ str(Te) + " y serian :")
print(LisTE)
print("La nueva lista que contiene las temperaturas por debajo tendria "+ str(Td) + " y serian :")
print(LisTD)
i = []
f = len(LisTE)
for t in range(0,f):
    p = LisTE[t]
    i.append(p)
f = len(LisTD)
for t in range(0,f):
    p = LisTD[t]
    i.append(p)
deN = deficit(i)
print("El deficit nuevo de temperatura es " + str(deN))
if deN == de :
    print("Los dos son iguales " + str(de) + " y "+ str(deN))
else :
    print("Los dos deficits son diferentes, el primero es "+ str(de) + " el segundo queda " + str(deN))
    