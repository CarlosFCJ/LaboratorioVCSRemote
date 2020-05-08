# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:23:15 2020

@author: CarlosC
"""
import random

cartas =  ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope","Bleach" , "Arc",
           "Fleming" , "Hardin" , "Robiar" , "Mccullough" , "Mooney"  ,"Reynolds"  ,  "Short" 
           ,  "Stanton"  ,  "Deadman"  , "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" 
           , "Powers" , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" , "Barnett" ,
           "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" , "Stone"  ,  "Cannon"  , "Garrison"
           ,  "Randall"  ,  "Leon"  ,  "Buck"  , "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" ,
           "Flowers" , "Whitehead"  ,  "Kirby"  ,  "Park"  ,  "Shannon"  ,  "Vlad"  ,  "Pepin" , 
           "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" , "Deleon"  ,  "Luke" 
           , "Lindsay"  ,  "Payne"  ,  "Gerbvo"  ,  "Hubbard"  , "Burnett", "Bryan" , "Ratliff" ,
           "Carlson" , "Parsons" , "Deadmeat" , "Crimson" , "Wilson" , "Terry" , "Hancock" ,
           "Hightower", "Burns" , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons" 
           ,"Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" , "Mcbride" , "Huffman" 
           , "Lightbringer" , "Blankenship", "Higgins" , "Saint"  ,  "Graham"  ,  "Hodor"  ,  "Ellison"
           ,"Roberts"  ,  "Odom"  , "Mann"]
premium = ["AIVLIS","LEIRBAG","NAILUJ", "SOLRAC", "ANAID"]

# Punto 1, usando el len() octengo el numero de elementos presente en la lista que selecione y luego imprimo un mensaje
# que me dice cuantos elemntos hay y cuales son
def imprimir(a):
    t = len(a)
    print("hay " + str(t) + " elementos y son " + str(a))
    
#Punto 3 usando random.choise en un ciclo hasta llegar al numero pedido y un if para revisar que el elemento no
# se encuentre ya en la lista 
def generador(l,N):
    lis = []
    for i in range(N):
        nu = random.choice(l)
        if nu not in lis :
            lis.append(nu)
    return lis
# Punto 5
def convinador(l,l1):
    t = len(l1)
    lit = []
    for i in range(t):
        lit.append(l1[i])
    t = len(l)
    for i in range(t):
        lit.append(l[i])
    random.shuffle(lit,random.random)
    return lit
def loteria():
    r = 0
    cp = 0
    g = int(len(cartas))
    y = int(len(premium))
    ccc = 0
    for i in range(0,g):
        cr = cartas[i]
        fa = 0
        for o in range(0,(len(paquete))):
            t = paquete[o]
            if t == cr :
                fa = fa + 1
        if fa >= 2 :
            r = r +1
    for i in range(0,y):
        cr = cartas[i]
        fa = 0
        for z in range(0,(len(paquete))):
            t = paquete[z]
            if t == cr :
                fa = fa + 1
                cp = cp +1
        if fa >= 2 :
            r = r +1
    if r >= 1 and cp <=1 :
        if random.randint(0,100)<10:
            aa = random.choice(premium)
            while ccc == 0 :
                for element in premium:
                    if element != aa :
                        ccc = ccc+1
            if ccc <= 4 :
                paquete.append(aa)
def pre(j,p):
    t = len(j)
    l = len(p)
    c = 0
    li = []
    for i in range(t):
        pd = j[i]
        for o in range(l):
            if pd == p[o]:
                c = c+1
                li.append(pd)
    cpre = c
    return cpre,li
def repe(j):
    c = 0
    o = len(j)
    for i in range(0,o):
        t = j[i]
        for m in range((i+1),o):
            if t == j[m] :
                c = c + 1
    print("se repirieron " + str(c) + " cartas")
def numero (j,c,p):
    t = len(j)
    y = len(c)
    u = len(p)
    li = []
    for i in range(0,t):
        li.append([(jugador[i]),0])
        k = (jugador[i])
        for n in range(0,y):
            if k == c[n]:
                li[i][1]= (li[i][1]) + 1
        for j in range(0,u):
            if k == p[j] :
                li[i][1] = (li[i][1]) +1
    print("hubieron estos numero de cada carta :")
    print(li)
def abc(AIV_original):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    p = len(AIV_original)
    o = len(abc)
    NABC = []
    for t in range(0,o):
        c = 0
        for y in range(0,p):
            i = str.lower(AIV_original[y][0])
            if abc[t] == i :
                c = c + 1
        ap = [(abc[t]),c]
        NABC.append(ap)
    print(NABC)
def marlargoycorto(AIV_original):
    f = len(AIV_original)
    t = len(AIV_original[0])
    c = 0
    for u in range(0,f):
        h = AIV_original[u]
        j = len(h)
        if t < j :
            t = j
            c = u
    m = AIV_original[c]
    print("la carta mas larga es " + str(m) + "con una longitud de "+str(t))
    y = len(AIV_original[0])
    it = 0
    for z in range(0,f):
        h = AIV_original[z]
        jn = len(h)
        if y > jn :
            y = jn
            it = z
    m = AIV_original[it]
    print("la carta mas corta es " + str(m) + "con una longitud de "+str(y))
def carpremiun(pr,pp,pi):
    if pr == 0:
        print("no obtuvo ninguna cartas premiun")
    else:
        p = len(pp)
        c = 0
        for t in range(0,pr):
            for y in range(0,p):
                i = str.lower(pp[y][0])
                f = str.lower(pi[t][-1])
                if f == i  :
                    c = c + 1
        print("el numero de cartas que empiezan con la ultima letras de la cartas premium que hay son " + str(0))
def retid2omas(cj,abecd):
    cty = []
    f = len(abecd)
    for g in range(0,f):
        contador = 0
        letra = abecd[g]
        fi = len(cj)
        for gt in range(0,fi):
            go = len(cj[gt])
            for yy in range(0,go):
                if yy != (go-1):    
                    if letra == (cj[gt][yy]) and letra == (cj[gt][(yy+1)]):
                        contador = contador + 1
        if contador > 0 :
                cty.append([letra,contador])
    print(cty)
def  ab(AIV_original) :
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    p = len(AIV_original)
    o = len(abc)
    NABC = []
    for t in range(0,o):
        c = 0
        for y in range(0,p):
            i = AIV_original[y]
            for element in i :
                if abc[t] == str.lower(element) :
                    c = c + 1
        NABC.append([(abc[t]),c])
    print(NABC)
# ------------------Ejecuciones-----------------------------------------------
imprimir(cartas)    
imprimir(premium)
jugador = generador(cartas,10)
imprimir(jugador)
juego = convinador(cartas,premium)
imprimir(juego)
sobre_uno = generador(juego,5)
sobre_dos = generador(juego,5)
sobre_tres = generador(juego,5)
lig = []
t = len(sobre_uno)
for i in range(t):
    lig.append(sobre_uno[i])
t = len(sobre_dos)
for i in range(t):
    lig.append(sobre_dos[i])
paquete = convinador(lig,sobre_tres)
loteria()
g = len(paquete)
for element in paquete:
    jugador.append(element)
pr,tli =pre(jugador,premium)
print("el jugador obtuvo este numero de cartas premiun " + str(pr) + " y fueron " + str(tli))
repe(jugador)
numero (jugador,cartas,premium)
abc(juego)
marlargoycorto(juego)
carpremiun(pr,juego,tli)
abcd = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
retid2omas(jugador,abcd)
ab(jugador)