import numpy as np 
import random 

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

def sacarVocales (s: str)->str:
    vocales: list = ["A","E","I","O","U","a","e","i","o","u"]
    res: str = ""
    for i in range (len(s)):
        if (pertenecestr(vocales, s[i])):
                res = res
        else:
                res = res + s[i]
    return res


def pertenecestr(s:list, e: str)->bool:
    res: bool = False
    for i in range(len(s)):
        if(s[i]==e):
            res: bool = True
    return res

# print(sacarVocales("hola"))
# print(sacarVocales("sebastian"))
# print(pertenecestr(["A","E","I","O","U","a","e","i","o","u"],"H"))


###4
"""
4. problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<"a","e","i","o","u">, s[i]) ∧ res[i] = " ") o
(¬ pertenece(<"a","e","i","o","u">, s[i]) ∧ res[i] = s[i] ) ) }
}
"""

def reemplazaVocales(s:[str])->[str]:
    vocales: list = ["A","E","I","O","U","a","e","i","o","u"]
    res: str = ""
    for i in range (len(s)):
        if (pertenecestr(vocales, s[i])):
                res = res + " "
        else:
                res = res + s[i]
    return res

# print(reemplazaVocales("hola"))
# print(reemplazaVocales("riquelme"))


###5
"""
problema daVueltaStr (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → res[i] = s[|s| - i - 1]}
}
"""

def daVueltaStr(s:[str])->[str]:
    res: str = ""
    for i in range(len(s)):
        res = res + s[len(s)-i-1] 
    return res

# print(daVueltaStr("hola"))
# print(daVueltaStr("libertadores"))


###6
"""
problema eliminarRepetidos (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: {(|res| ≤ |s|) ∧ (para todo i ∈ Z si 0 ≤ i < |s| → pertenece(s[i], res)) ∧ (para todo i, j ∈ Z si
(0 ≤ i, j < |res| ∧ i 6= j) → res[i] 6= res[j])}
}
"""

def eliminarRepetidos(s:[str])->[str]:
    res= ""
    for i in range(len(s)):
        if(pertenece(res,s[i])):
            res = res
        else:
            res = res + s[i]
    return res

# print(eliminarRepetidos("sebastian"))
# print(eliminarRepetidos("aeiouaeiou"))

##############EJ 3

def aprobado(notas:[int])->int:
    res:int=0
    if (todosMayoresA4(notas) and promedio(notas)>=7):
        res=1
    elif (todosMayoresA4(notas) and 4<=promedio(notas)<7):
        res = 2
    else:
        res = 3
    return res



def todosMayoresA4 (notas: [int])->bool:
    res: bool = True
    for i in range(len(notas)):
        if (notas[i]<4):
            res = False
    return res


def promedio (notas:[int])->float:
    res = 0
    for i in range(len(notas)):
        res = res + notas[i]
    res = res / (len(notas))
    return res

# print(todosMayoresA4([4,5,6,7,8,9]))
# print(todosMayoresA4([4,5,6,1,8,9]))
# print(promedio([8,10,10,9,9,8]))
# print(aprobado([8,9,10,7,5]))


#################EJ 4

###1
def alumnos()->[str]:
    res: [str]= []
    nombre: str = (input("Nombre:"))
    while (nombre != "listo"): 
        res.append(nombre)
        nombre =str(input("Nombre:"))
    return res


###2

def sube()->[tuple]:
    res:[tuple] = []
    movimiento: str = input("Que quiere hacer?")
    while (movimiento != "X"):
        if (movimiento == "C"):
            monto: int = input("Ingresar monto")
            res.append(("C",monto))
            movimiento: str = input("Que quiere hacer?")
        else:
            monto: int = input("Ingresar monto")
            res.append(("D",monto))
            movimiento: str = input("Que quiere hacer?")
    return res


###3

def sumaDelJuego(x:float, y:float)->float:
    res: int = x
    if (y>=10):
        res = res + 0.5
    else:
        res = res + y
    return res
        


def sieteYmedio()->[int]:
    
    contador: int = 0
    numeros: [int] = [1,2,3,4,5,6,7,10,11,12]
    primerCarta: int = random.choice(numeros)
    print("Tu carta es", str(primerCarta))
    res: [int] = [primerCarta]
    contador = sumaDelJuego(0,primerCarta)
    print("Y vas",str(contador))
    siguientePaso: str = input("Que vas a hacer?")
                               
    while (siguientePaso == "sigo" and contador<7.5):
        otraCarta: int = random.choice(numeros)
        print("Tu carta es", str(otraCarta))
        res.append(int(otraCarta))
        contador = sumaDelJuego(contador,otraCarta)
        if (contador < 7.5):
            print("Y vas",str(contador))
            siguientePaso: str = input("Que vas a hacer?")
    
    if(contador == 7.5):
        print("GANASTE!")
    elif(contador<7.5):
        print("CORTO")
    else:
        print("PERDISTE!!")
    return res


#################EJ 5

###1 
"""
problema perteneceACadaUno (in s:seq<seq<Z>>, in e:Z, out res: seq<Bool>) {
requiere: { True }
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ pertenece(s[i], e))}
}
"""

def perteneceACadaUno (s:[[int]], e: int, res:[bool]):
    res = []
    for i in range (len(s)):
        res.append(pertenece(s[i],e))
    print(res)
   

###2
"""
problema esMatriz (in s:seq<seq<Z>>) : Bool {
requiere: { T rue }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}
}

"""

def esMatriz (s:[[int]])->bool:
    res: bool = True
    if (len(s) == 0 or len(s[0]) == 0):
        res = False
    for i in range(len(s)):
        if (len(s[0]) != len(s[i])):
            res = False
    return res

# print(esMatriz([[1,2,3],[2,2,2]]))
# print(esMatriz([[1,2,3,4],[2,2,2]]))
# print(esMatriz([[],[2,2,2]]))

###3

"""
3. problema filasOrdenadas (in m:seq<seq<Z>>, out res: seq<Bool>) {
requiere: { es Matriz(m)}
asegura: { Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}
"""                      

def filasOrdenadas(m:[[int]], res:[bool]):
    res = []
    for i in range (len(m)):
        if (ordenados(m[i])):
            res.append(True)
        else:
            res.append(False)
    print(res)

# filasOrdenadas([[1,2,3],[4,5,6]],[True,False])
# filasOrdenadas([[1,2,3],[4,1,6]],[True,False])


###4

def elevarMatrices (d: int, p:int)->[[float]]:
    m = np.random.random((d, d))**2
    if (p == 0):
        res: [[int]] = np.identity(d)
    else:
        res: [[int]] = m
        for i in range (1,p+1):
            if (p == 1):
                res = res
            else:
                res: [[int]] = multiplicacionDeMatrices(res,m)
    return res




def multiplicacionDeMatrices (a:[[int]], b:[[int]]):
    res: [[int]] = np.random.random((len(b[0]),len(a)))
    for i in range (len(a)):
        for k in range (len(b)):
            valor = 0
            for j in range (len(a[i])):
                valor = valor + a[i][j] * b[j][k]
                res[i][k] = valor
    return res

from queue import LifoQueue as Pila

################EJ 1

"""
Una funcion contar lineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de lineas de texto del
archivo dado
"""






###############EJ 2

def clonar_sin_comentarios (nombreArchivo:str):
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()

    archivo_nuevo = []
    for l in lineas:
        s = l.strip()

        if len(s) == 0 or (not "#" == s[0]):
            archivo_nuevo.append(l)

    archivo.close()
    salida = open("sincomentarios.txt", "w")
    for l in archivo_nuevo:
        salida.write(l)
    salida.close()

#clonar_sin_comentarios("ejemploComentado.py")

##############EJ 10

#creando pila

p= Pila ()
p .put(1) #apilar
p. put(2)
p. put(1)
elemento = p .get() #desapilar
p .empty () #vacia?



def buscar_el_maximo(pila: Pila)->int:
    maximo: int = p.get()

    while not p.empty():
        i : int = p.get()
        if maximo < i:
            maximo = i

    return maximo

#print(buscar_el_maximo(p))

###############EJ 19



def agrupar_por_longitud (nombre_archivo:str)->dict:
    archivo = open(nombre_archivo, "r")
    lineas = archivo.readlines()

    d = {}

    for l in lineas:
        for palabra in l.split():
            if len(palabra) in d:
                d[len(palabra)] = d[len(palabra)] + 1
            else:
                d[len(palabra)] = 1
    
    archivo.close()
    return d 

print(agrupar_por_longitud("boca.py"))

    
    

print(elevarMatrices(2,2))
print(multiplicacionDeMatrices([[5,2,1],[2,1,2],[4,1,3]],[[1,4,2],[0,3,0],[2,1,3]]))
