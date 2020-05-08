# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:55:44 2020

@author: Carlos
"""
familia = {"JuanF":[126,131,123,120] ,
           "Amparo":[151,130],
           "Antonio":[110],
           "MariaJ":[98,122,115],
           "LisaF":[123,130],"Leonardo":[121,133]
           , "JavierC":[121,133],"SantiagoA":[123,115]
           }
# Punto 1
miFa = ["JuanF","Amparo","Antonio","MariaJ","LisaF","Leonardo","JavierC","SantiagoA"]
q = miFa[0]
c = len(familia[q])
for f in range(0,(len(familia))):
    t = len(familia[miFa[f]])
    if c < t :
        c = t
        q = miFa[f]
print("El miembro de la familia que se ha realizado más exámenes  es "+ str(q) + " con " + str(c)
      + " pruebas")
for f in range(0,(len(familia))):
    t = len(familia[miFa[f]])
    if c > t :
        c = t
        q = miFa[f]
print("El miembro de la familia que se ha realizado menos exámenes es "+ str(q) + " con " + str(c)
      + " pruebas")

#Punto 2

PrFa = {}
for element in familia:
    PrFa[element] = round(sum(familia[element])/len(familia[element]),2)
Dt = {}
for element in PrFa:
    if PrFa[element] > 126 :
        Dt[element] = PrFa[element]
print("La personas de la familia que se visualiza que presentan diabetes son ")
print(Dt)

#Punto 3
PD = {}
for element in PrFa:
    if PrFa[element] < 126 and PrFa[element] > 109 :
        PD[element] = PrFa[element]
print("La personas en la familia que pueden ser prediabetes ")
print(PD)

