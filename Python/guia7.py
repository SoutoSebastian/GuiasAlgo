import numpy as np 

#####EJ 1 

#1. problema pertenece (in s:seq<Z>, in e: Z) : Bool {
#requiere: { T rue }
#asegura: { (res = true) ↔(existe un i ∈ Z tal que 0 ≤ i < |s| ∧ s[i] = e)}
#}
#Implementar al menos de 3 formas distintas este problema.
#¿Si la especificaramos e implementaramos con tipos genericos, se podrıa usar esta misma funcion para buscar un
#caracter dentro de un string? SI funciona. 

#forma1
def pertenece1(s:list, e:int)->bool:
    for i in range (len(s)):
        if(s[i] == e):
            res:bool = True
            break
        else:
            res :bool =False
            
    return res

#forma2
def pertenece(s:list, e:int)->bool:
    res: bool = False
    for i in range(len(s)):
        if(s[i]==e):
            res: bool = True
    return res


#test1 = pertenece([1,2,3], 2)
#print(test1)
#test2 = pertenece([1,2,3], 3)
#print(test2)
#test3 = pertenece([1,2,3], 1)
#print(test3)
#test4 = pertenece([1,2,3], 6)
#print(test4)



####EJ 2 

# 2. problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
# requiere: {e /= 0 }
# asegura: { (res = true) ↔ (para todo i ∈ Z si 0 ≤ i < |s| → s[i] mod e = 0)}
# }

def divideATodos1(s:list, e:int)->bool:
    for i in range(len(s)):
        if (s[i]%e != 0):
            res :bool = False
            break
        else:
            res = True
    return res


def divideATodos(s:list, e:int)->bool:
    res = True
    for i in range(len(s)):
        if (s[i]%e != 0):
            res = res and False
        else:
            res = res and True
            
    return res

# test5 = divideATodos([2,4,6], 2)
# print(test5)
# test6 = divideATodos([2,4,6], 3)
# print(test6)


####3
# 3. problema sumaTotal (in s:seq<Z>) : Z {
# requiere: { T rue }
# asegura: { res es la suma de todos los elementos de s}
# }

def sumaTotal1 (s:list)->int:
    suma = 0
    for i in s:
        suma += i
    return suma


def sumaTotal (s:[int])->int:
    res :int = 0
    for i in range(len(s)):
        res += s[i]
    return res


#test7 = sumaTotal([1,2,3])
#print(test7)


###4
# 4. problema ordenados (in s:seq<Z>) : Bool {
# requiere: { T rue }
# asegura: { res = true ↔(para todo i ∈ Z si 0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
# }

def ordenados(s: list)->bool:
    res = True
    for i in range (len(s)):
        if (i == (len(s)-1)):
            res = res
        elif ((s[i])< (s[i+1])):
            res = res and True
        else:
            res = res and False
    return res

"""
test8 = ordenados([1,2,3])
print(test8)
print(ordenados([2,1,5]))
print(ordenados([1,2,3,4,5,6,4]))
"""


###5
#Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7.

def palabraLarga(s:[str])->bool:
    res:bool = False
    for i in range (len(s)):
        if (len(s[i])>7):
            res = True
    return res

#print (palabraLarga(["hola", "como", "estas", "septimalibertadores"]))

###6
#Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
#contrario.

def palindromo (text :str)->bool:
    res: bool = True
    for i in range (len(text)):
        if (text[i] != text[len(text)-1-i]):
            res = False
    return res

#print(palindromo("hola como estas como hola"))
#print(palindromo("hola aloh"))

###7

"""
7. Analizar la fortaleza de una contrasena. El parametro de entrada de la funcion sera un string con la contrasena a
analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “n/ N”
es considerado un caracter especial y no se comporta como cualquier otra letra.
La contrasena sera VERDE si:
a) la longitud es mayor a 8 caracteres
b) tiene al menos 1 letra minuscula.
c) tiene al menos 1 letra mayuscula.
d ) tiene al menos 1 digito numerico (0..9)
La contrasena sera ROJA si:
a) la longitud es menor a 5 caracteres.
En caso contrario sera AMARILLA
"""

def contraseña(s:str)->str:
    if(minus(s) and mayus(s) and num(s) and len(s)>8):
        res:str = "VERDE"
    elif (len(s)<5):
        res:str = "ROJA"
    else:
        res:str = "AMARULLA"
    return res


def minus(s:str)->bool:
    res = False
    for i in range (len(s)):
        if (s[i]>='a' and s[i]<='z'):
            res = True
    return res


def mayus(s:str)->bool:
    res = False
    for i in range (len(s)):
        if (s[i]>='A' and s[i]<='Z'):
            res = True
    return res


def num(s:str)->bool:
    res = False
    for i in range (len(s)):
        if (s[i]>='0' and s[i]<='9'):
            res = True
    return res

#print(contraseña("Hola123boca"))
#print(contraseña("hola"))
#print(contraseña("chinos"))

###8

"""
Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
dinero y “R” para retiro de dinero, y ademas el monto de cada operacion. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280
"""

def saldoActual(mov: list)->int:
    saldo = 0
    for i in range(len(mov)):
        if (esI(mov[i])):
            saldo += (mov[i])[1]
        elif (esR(mov[i])):
            saldo -= (mov[i])[1]
        else:
            saldo = saldo
    return saldo




def esR(v:tuple)->bool:
    res: bool = False
    if (v[0] == "R"):
        res: bool = True
    return res

def esI(v: tuple)->bool:
    res: bool = False
    if(v[0] == "I"): 
        res: bool = True
    return res

#print(esI(("I",20)))
#print(saldoActual([("I",20)]))
#print(saldoActual([("I",20),("R",10),("I",10)]))


###9
#Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y False en caso
#contrario

def vocalesDistintas(palabra: str)->bool:
    vocales = ["A","E","I","O","U","a","e","i","o","u"]
    res = 0
    resultado = False
    for i in range(len(vocales)):
        for j in range(len(palabra)):
            if (palabra[j] == vocales[i]):
                res +=1
                vocales[i] = ""
    if (res>=3):
        resultado = True
    return resultado

#print(vocalesDistintas("patocuak"))
#print(vocalesDistintas("boca"))
#print(vocalesDistintas("AEPELE"))
#print(vocalesDistintas("aex"))

##################EJ 2

###1
#Dada una lista de n´umeros, en las posiciones pares borra el valor original y coloca un cero. Esta funci´on modifica el
#par´ametro ingresado, es decir, la lista es un par´ametro de tipo inout.

def pospares (s: [int]): 
    for i in range(len(s)):
        if (i%2 == 0):
            s[i] = 0


###2
#Lo mismo del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista, igual a la anterior
#pero con las posiciones pares en cero, es decir, la lista pasada como par´ametro es de tipo in

def pospares2 (s: [int])->[int]:
    res = s.copy()
    for i in range(len(res)):
        if (i%2 == 0):
            res[i] = 0
    return res

#print(pospares2([1,2,3,4,5,6,7,8,9]))


###3
#Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios,
#sino que borra la vocal y concatena a continuaci´on
