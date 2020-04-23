# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:10:19 2020

@author: Carlos
"""
import numpy as np

# punto 1 la funcion generador usa los parametros que sele ingresan para general un arreglo de datos
# aleatorios enteros  mediante el comando np.random.randint
def generador(a,b):
    f = np.random.randint(a,b,(4,12))
    return f
ingresos = generador(100,180)

egresos = generador(60,130)

def imprimir(a):
    dias = np.array(["         ","Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic"])
    Ciudadd = np.array(["Bucaramanga ","Floridablanca","Giròn        ","Piedecuesta  "])
    f = len(Ciudadd)
    for r in range(0,f):
        print(dias)
        print(str(Ciudadd[r]) + str(a[r]) + "\n")
print("Los Ingresos son ")
imprimir(ingresos)
print("Los egresos son ")
imprimir(egresos)
def restador(a,b):
    P = a - b
    return P
ganancias = restador(ingresos,egresos)

print("Las ganancias son :")

imprimir(ganancias)

def mejor_ciudad(a) :
    n = len(a[0])
    MC = 0
    mac = 0
    c = 0
    for t in range(0,4) :
        c = 0
        for o in range(0,n):
            c = c + a[t,o]
        if MC < c :
            MC = c
            mac = t
    return mac
Ciuda = np.array(["Bucaramanga","Floridablanca","Giròn","Piedecuesta"])
Mayot = mejor_ciudad(ganancias)
print("La ciudad con mayores ganancias es " + str(Ciuda[Mayot]))

def menor_ciudad(a) :
    n = len(a[0])
    MC = 0
    mac = 0
    c = 0
    for t in range(0,4) :
        c = 0
        for o in range(0,n):
            c = c + a[t,o]
        if MC > c :
            MC = c
            mac = t
    return mac
menot = menor_ciudad(ganancias)
print("La ciudad con menores ganancias es " + str(Ciuda[menot]))

def mejor_mes(a,b) :
    dias = np.array(["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
                     "Octubre","Noviembre","Diciembre"])
    n = len(a[0])
    for t in range(0,4) :
        c = 0
        MC = 0
        for o in range(0,n):
            c = a[t,o]
            if MC < c :
                MC = c
                mac = t
                ms = o
        print("El mejor mes que tuvo la ciudad " + str(b[mac]) + " es " + str(dias[ms])+ "\n")
mejor_mes(ganancias,Ciuda)

def peor_mes(a,b) :
    dias = np.array(["Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
                     "Octubre","Noviembre","Diciembre"])
    n = len(a[0])
    for t in range(0,4) :
        MC = 0
        mac = t
        ms = 0
        for o in range(0,n):
            c = a[t,o]
            if c < MC :
                MC = c
                ms = o
        print("El peor mes que tuvo la ciudad " + str(b[mac]) + " es " + str(dias[ms]) + "\n")
peor_mes(ganancias,Ciuda)

def imprimir_personalizado(a,b,c) :
    dias = np.array(["         ","Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
    Ciudadd = np.array(["Bucaramanga ","Floridablanca","Giròn        ","Piedecuesta  "])
    for r in range(0,4):
        print("             " + str(dias[range(b,(c+1))]))
        print(str(Ciudadd[r]) + str(a[r,[range((b-1),c)]]) + "\n")
imprimir_personalizado(ganancias,3,6)
def imprimir_personalizado(ganancias, z, w):
    ciudad, mes = ganancias.shape
    ciudades = ["Bucaramanga  ", "Floridablanca", "Girón        ",
                         "Piedecuesta  "]
    meses = ['         ', 'Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago',
             'Sep', 'Oct', 'Nov', 'Dic']
    print("\n" + str(meses[0]) + str(meses[z: w+1]))
    for i in range(0, ciudad):
        print(str(ciudades[i]) + str(ganancias[i, z-1:w]))

def promedio(ingresos, egresos, ganancias):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", 
             "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    citys = ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"]
    print('\n')
    for i in range(0, len(citys)):
        suma = 0
        for k in range(0, len(meses)):
            suma = (suma + ingresos[i, k])
        promedio = suma/len(meses)
        print('El promedio de ingresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
    print('\n')
    for i in range(0, len(citys)):
        suma = 0
        for k in range(0, len(meses)):
            suma = (suma + egresos[i, k])
        promedio = suma/len(meses)
        print('El promedio de egresos de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))
    print('\n')
    for i in range(0, len(citys)):
        suma = 0
        for k in range(0, len(meses)):
            suma = (suma + ganancias[i, k])
        promedio = suma/len(meses)
        print('El promedio de ganancias de la ciudad ' + str(citys[i]) + 
              ' es: ' + str(round(promedio, 2)))


