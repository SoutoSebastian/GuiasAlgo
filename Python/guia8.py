from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from random import shuffle
##################################PARTE 1: ARCHIVOS

################EJ 1

#1
"""
Una funcion contar lineas(in nombre archivo : str) → int que cuenta y devuelva la cantidad de lineas de texto del
archivo dado
"""

def contar_lineas (nombreArchivo:str)->int:
    archivo = open(nombreArchivo , "r")
    lineas = archivo.readlines()
    res = len(lineas)
    return res

#print(contar_lineas("probando.py"))

#2
def existe_palabra (palabra:str, nombreArchivo:str)->bool:
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    res:bool = False
    
    for l in lineas:
        if palabra in l:
            res = True
    return res

# print(existe_palabra("como","probando.py"))
# print(existe_palabra("boca","probando.py"))

#3
def cantidad_de_apariciones (nombreArchivo:str, palabra:str)->int:
    archivo = open(nombreArchivo, "r")
    lista = archivo.readlines()
    res: int = 0
    
    for linea in lista :
        for palabraEnArchivo in linea.split():
            if palabra == palabraEnArchivo:
                res += 1
    
    return res

# print(cantidad_de_apariciones("probando.py","hola"))
       
       

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

# clonar_sin_comentarios("probando.py")


###############EJ 3

def dar_vuelta (nombreArchivo :str):
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    salida = open("reverso.txt","w")
    lista = []
    archivo.close()
    
    for l in lineas:
        lista.append(l)
    print(lista)
    
    for i in range (len(lista)):
        if i != 0:
            salida.write(lista[len(lista)-1-i])
        else:
            salida.write(lista[len(lista)-1-i] + '\n')
    salida.close()
    

#dar_vuelta("probando.py")


###############EJ 4

def agregar_frase(nombreArchivo:str, frase:str):
    archivo = open(nombreArchivo, "a")
    archivo.write('\n' + frase)
    archivo.close

# agregar_frase("probando.py", "esto es boca")

###############EJ 5

def agregar_frase2(nombreArchivo:str, frase:str):
     archivo = open(nombreArchivo, "r")
     listaDeLineas = archivo.readlines()
     archivo.close()
    
     archivo = open(nombreArchivo, "w")
     archivo.write(frase + '\n')
     
     for l in listaDeLineas:
         archivo.write(l)
     archivo.close

# agregar_frase2("probando.py", "esto es boca")

###############EJ 6

def modo_binario(nombreArchivo:str)->list:
    archivo = open(nombreArchivo, "b")
    listaLineas = archivo.readlines()
    res: list = []
    archivo.close
    
    for l in listaLineas:
        listaPalabras = l.split()
        for i in listaPalabras:
            if esvalida(chr(listaPalabras[i])):
                res.append(listaPalabras[i])
    
    return res
    


def esvalida(palabra: str)-> bool:
    res: bool = True
    if (len(palabra)<5):
        res = False
    
    for i in range (len(palabra)):
        if not ('a'<=palabra[i]<='z'):
            if not ('A'<=palabra[i]<='Z'):
                if not ('1'<=palabra[i]<='9'):
                    if not (palabra[i] == ' ' or palabra[i] == '_'):
                        res = False              
        
    return res

###############EJ 7

def promedio_estudiante (lu: str)->float:
    archivo = open("notas.csv","r", encoding = "utf8")
    listaDeLineas = archivo.read()
    notas: list = listaDeLineas.split('\n')
    sumaNotas : int = 0
    divisor : int = 0
    
    for nota in notas:
        alumno = nota.split(',')
        if alumno[0] == lu:
            sumaNotas += float(alumno[3])
            divisor +=1
            
    if divisor == 0:
        res = -1
    else:
        res = sumaNotas/divisor
    
    return res

# print(promedio_estudiante("822/22"))

# def probando ()->list:
#     archivo = open("notas.csv","r", encoding = "utf8")
#     listaDeLineas = archivo.readlines()
    
#     return listaDeLineas

# print(probando())
    
##################################PARTE 2: PILAS

#creando pila

p= Pila ()
p .put(1) #apilar
p. put(2)
p. put(3)
elemento = p .get() #desapilar
p .empty () #vacia?

def imprimirPila (p:Pila):
    while not(p.empty()):
        elemento = p.get()
        print(elemento)

# imprimirPila(p)

##############EJ 8

def generar_numeros_al_azar (n:int, desde:int, hasta:int)->Pila:
     p = Pila()
     listaApoyo: [int] = []
    
     while len(listaApoyo) < n :
         x = random.randint(desde,hasta)
         p.put(x)
         listaApoyo.append(x)
     
    #  imprimirPila(p)
     print(listaApoyo)     
     return p
    
#otra forma

def generar_numeros_al_azar2 (n:int, desde:int, hasta:int)->Pila:
    p = Pila()
    
    for i in range (n):
        x = random.randint(desde,hasta)
        p.put(x)
    
    # imprimirPila(p)
    return p
        
# generar_numeros_al_azar(5,1,10)

##############EJ 9

def cantidad_de_elementos(p: Pila)-> int:
    res:int = 0
    apoyo: list = []
    while not(p.empty()):
        elemento = p.get()
        apoyo.append(elemento)
        res += 1
    
    for i in range (len(apoyo)):
        p.put(apoyo[len(apoyo)-1-i])
    

        
    return res

# prueba = generar_numeros_al_azar(4,1,3)
# print(cantidad_de_elementos(prueba))
# print(prueba.empty())
# print(prueba.get())
# print(prueba.get())
# print(prueba.get())
# print(prueba.get())


##############EJ 10


def buscar_el_maximo(p: Pila)->int:
    apoyo = []
    maximo: int = p.get()
    apoyo.append(maximo)

    while not p.empty():
        i : int = p.get()
        apoyo.append(i)
        if maximo < i:
            maximo = i
    
    for i in range (len(apoyo)):
        p.put(apoyo[(len(apoyo))-1-i])
        
    return maximo

# print(buscar_el_maximo(p))


###############EJ 11

def esta_bien_balanceada(s:str)->bool:
    res: bool = (balanceo_operaciones(s) and balanceo_parentesis(s))
    return res
#condiciones: tiene que haber espacios entre cada operacion, y depues de los parentesis no hay espacios, no importa que caracter le sigue.

def balanceo_operaciones(s:str)->bool:
    operaciones : list = ['*','/','+','-']
    res: bool = True
    p = Pila()
    q = Pila()
    for i in range (len(s)):
        p.put(s[i])
    
    for i in range(len(s)):
        q.put(s[len(s)-1-i])
    
    while not p.empty():
        elemento = p.get()
        if elemento in operaciones:
            otro = p.get()
            if otro != ' ':
                res = False
            elif otro == ' ':
                if p.get() == '(':
                    res = False
                                    
    while not q.empty():
        elemento = q.get()
        if elemento in operaciones:
            otro = q.get()
            if otro != ' ':
                res = False
            elif otro == ' ':
                if q.get() == ')':
                    res = False
    #print(res)
    return res
            
# balanceo_operaciones("2 + 2")


def balanceo_parentesis(s:str)->bool:
    res: bool = True
    p = Pila()
    q = Pila()
    
    for i in range (len(s)):
        p.put(s[i])
        q.put(s[len(s)-1-i])
    
    while not (p.empty()):
        elemento = p.get()
        if elemento == '(':
            if p.empty():
                res = True
            elif p.get() == ')':
                res = False
                break
        elif elemento == ')':
            if p.empty():
                res = False
            elif p.get() == '(':
                res = False
                break
    
    #print(res)
    return res

# balanceo_parentesis(')2+2(')
# balanceo_parentesis('(()2+2))')
# balanceo_operaciones('1 + ) 2 x 3 ( ()')

# print(esta_bien_balanceada('2 + 2 / (5 - 2)'))
# print(esta_bien_balanceada('1 + ( 2 x 3 - ( 2 0 / 5 ) )'))
# print(esta_bien_balanceada('1 + ) 2 x 3'))
# print(esta_bien_balanceada('(2 + )'))


###############EJ 12

def postfix(s:str)->float:
    tokens = s.split(' ')
    p = Pila()
    operadores :list = ['+', '-', '*', '/']
    for i in tokens:
        if not (i in operadores):
            p.put(i)
        elif i == '+':
            primerElemento = p.get()
            resu = int(primerElemento) + int(p.get()) 
            p.put(resu)
        elif i == '-':
            primerElemento = p.get()
            resu = int(p.get()) - int(primerElemento) 
            p.put(resu)
        elif i == '*':
            primerElemento = p.get()
            resu = int(primerElemento) * int(p.get())
            p.put(resu)
        elif i == '/':
            primerElemento = p.get()
            resu = float(p.get()) / float(primerElemento)
            p.put(resu)           
    print(p.get())


# postfix('3 4 +')
# postfix('3 4 + 5 * 2 -')
# s = '3 4 +'
# tokens = s.split(' ')
# print(tokens)


##################################PARTE 3: COLAS

###############EJ 13

def cola_random (n:int, desde:int, hasta:int)->Cola:
    c = Cola()
    p = generar_numeros_al_azar2(n,desde,hasta)
    for i in range(n):
        elemento: int = p.get()
        c.put(elemento)
    
    return c

# cola =cola_random(3, 1, 4)
# print(cola.get())
# print(cola.get())
# print(cola.get())


###############EJ 14

def cantidad_de_elementos_cola(c: Cola)->int:
    apoyo: list = []
    res: int = 0 
    while not (c.empty()):
        elemento = c.get()
        apoyo.append(elemento)
        res += 1
        
    for i in range (len(apoyo)):
        c.put(apoyo[i])
        
    return res

# print(cantidad_de_elementos_cola(cola))
# print(cola.get())
# print(cola.get())
# print(cola.get())


###############EJ 15

def buscar_el_maximo_cola (c: Cola)->int:
    maximo = c.get()
    apoyo: list = []
    apoyo.append(maximo)
    while not (c.empty()):
        elemento = c.get()
        apoyo.append(elemento)
        if maximo<elemento:
            maximo = elemento
    
    for i in range(len(apoyo)):
        c.put(apoyo[i])
    
    print(apoyo)
    print(maximo)
    return maximo

# colita = Cola()
# colita.put(1)
# colita.put(2)
# colita.put(10)
# colita.put(5)
# colita.put(2)
# print("original")
# print(colita.get())
# print(colita.get())
# print(colita.get())
# print(colita.get())
# print(colita.get())
# buscar_el_maximo_cola(colita)
# print(buscar_el_maximo(colita))
# print("despues")
# print(colita.get())
# print(colita.get())
# print(colita.get())
# print(colita.get())
# print(colita.get())


###############EJ 16 BINGO 
#un carton tiene 12 numeros al azar

def armar_secuencia_de_bingo()->Cola:
    listilla: [int] = []
    c = Cola()
    for i in range (99):
        listilla.append(i)
    
    random.shuffle(listilla)
    print(listilla)
    
    for i in range (len(listilla)):
        c.put(listilla[i])
        
    return c


def jugar_carton_de_bingo(carton:[int], bolillero: Cola)->int:
    res :int = 0
    contador = 0

    for i in range (99):
        while (contador < 12):
            numero:int = bolillero.get()
            res += 1
            for j in range(len(carton)):
                if numero == carton[j]:
                    contador += 1
                               
    print(res)
    return res

        
# bolillero = armar_secuencia_de_bingo()
# carton = [2, 24, 32, 6, 12, 47, 86, 93, 55, 43, 37, 10]
# carton2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# jugar_carton_de_bingo(carton2, bolillero)


###############EJ 17

def n_pacientes_urgentes(c:Cola)->int:
    res:int = 0
    while not (c.empty()):
        paciente = c.get()
        if  1<=paciente[0]<=3:
            res += 1
    
    return res

# pacientes = Cola()
# pacientes.put((7,"s","j"))
# pacientes.put((6,"s","j"))
# pacientes.put((5,"s","j"))
# pacientes.put((5,"s","j"))

# print(n_pacientes_urgentes(pacientes))


###############EJ 18

def a_clientes(ingreso: Cola)->Cola:
    atendidos = Cola()
    listilla: list = []
    
    while not (ingreso.empty()):
        cliente = ingreso.get()
        listilla.append(cliente)
        
    print (listilla)
    for i in range (len(listilla)):
        if listilla[i][3] == True:
            atendidos.put(listilla[i])

    for i in range (len(listilla)):
        if (listilla[i][2] == True) and (listilla[i][3] != True):
            atendidos.put(listilla[i])
    
    for i in range(len(listilla)):
        if (listilla[i][2] != True) and (listilla[i][3] != True):
            atendidos.put(listilla[i])
    
    return atendidos

# ingreso = Cola()
# ingreso.put(("s",1,True,True))
# ingreso.put(("s",5,False,False))
# ingreso.put(("s",2,True,False))
# ingreso.put(("s",3,False,False))
# ingreso.put(("j",6,True,True))
# atendidos = a_clientes(ingreso)
# print(atendidos.get())
# print(atendidos.get())
# print(atendidos.get())
# print(atendidos.get())
# print(atendidos.get())
        
##################################PARTE 4: DICCIONARIOS

###############EJ 19

def agrupar_por_longitud(nombreArchivo: str)->dict:
    archivo = open(nombreArchivo, "r")
    listaLineas = archivo.readlines()
    d = {}
    
    for l in listaLineas:
        palabras = l.split()
        for palabra in palabras:
            if len(palabra) in d:
                d[len(palabra)] += 1
            else:
                d[len(palabra)] = 1
    
    archivo.close()
    return d

# print(agrupar_por_longitud("hola"))


###############EJ 20

def promedio_todos ()->dict:
    archivo = open("notas.csv","r", encoding="utf8")
    listaLU : [str] = []
    todo = archivo.read()
    lineas = todo.split('\n')
    archivo.close()
    
    for l in lineas:
        palabras = l.split(',')
        if not (palabras[0] in listaLU):
            listaLU.append(palabras[0])
    
    print(listaLU)
    d = {}
    
    for LU in listaLU:
        d[str(LU)] = promedio_estudiante(str(LU))
    
    return d


def promedio_estudiante(lu:str)->float:
    archivo = open("notas.csv","r",encoding="utf8")
    todo = archivo.read()
    lineas = todo.split('\n')
    sumaNotas: int = 0
    divisor: int = 0
    
    for l in lineas:
        elementos = l.split(',')
        if elementos[0] == lu:
            sumaNotas += int(elementos[3])
            divisor += 1
    
    res:float = sumaNotas/divisor
    return res

# print(promedio_estudiante("822/22"))
    
# print(promedio_todos())


###############EJ 21

def la_palabra_mas_frecuente(nombreArchivo: str)-> str:
    archivo = open(nombreArchivo, "r")
    lineas = archivo.readlines()
    d = {}
    
    for l in lineas:
        palabras = l.split()
        for palabra in palabras:
            if palabra in d:
                d[palabra] += 1
            else:
                d[palabra] = 1
    res = obtener_maxima_key(d)
    return res



def obtener_maxima_key (d:dict)->str:
    maximo = 0
    res = ""
    
    for key in d:
        if d[key]>maximo:
            maximo=d[key]
            res = key
            
    return res

d = {'hola':10,
    'cgau': "dios",
    'hoy':1.5,
    'ayer':[1,232]}

# d['nuevo'] = d
# d['hola'] = 2
# print(d['hola'])
# print(d['nuevo'])

# print(d)

# print(obtener_maxima_key(d))

# print(la_palabra_mas_frecuente("hola"))


###############EJ 22

#1
usuario1 = Pila()
usuario1.put("soysocio")
usuario1.put("siu")
usuario1.put("gmail")

usuario2 = Pila()
usuario2.put("soysocio")
usuario2.put("pronostico")
usuario2.put("python")

usuario3 = Pila()
usuario3.put("youtube")
usuario3.put("tiktok")
usuario3.put("ig")
# print(usuario1.queue)

historiales = {"juan":usuario1, "carlos":usuario2, "rober":usuario3}

#2

def visitar_sitio(historiales:dict, usuario:str,sitio:str):
    if usuario in historiales:
        historiales[usuario].put(sitio)
    else:
        historiales[usuario]=Pila()
        historiales[usuario].put(sitio)
        
visitar_sitio(historiales, "yo", "twitter")
# print(historiales)
visitar_sitio(historiales,"yo","soysocio")
# print(historiales["yo"].get())
# visitar_sitio(historiales,"juan","mlibre")
# print(historiales["juan"].get())
#3

#OPCION 1 

def navegar_atras(historiales:dict, usuario:str):
    viejo_sitio = historiales[usuario].get()
    historiales["navegacion_trasera" + str(usuario)] = viejo_sitio


navegar_atras(historiales, "yo")
# print(historiales["yo"].get())
# print(historiales["navegacion_traserayo"])

#OPCION 2

def navegar_atras2(historiales:dict,usuario:str):
    ultimo_sitio = historiales[usuario].get()
    futuro_sitio = historiales[usuario].get()
    historiales[usuario].put(futuro_sitio)
    historiales[usuario].put(ultimo_sitio)
    historiales[usuario].put(futuro_sitio)
    
# navegar_atras2(historiales, "yo")
# print(historiales["yo"].get())
# print(historiales["yo"].get())
# print(historiales["yo"].get())

#4

#OPCION 1 (va con la opcion 1 del anterior)

def navegar_adelante(historiales:dict,usuario:str):
    historiales[usuario].put(historiales['navegacion_trasera'+str(usuario)])

# navegar_adelante(historiales,"yo")
# print(historiales["yo"].get())


#probando
"""navegar_atras(historiales, "juan")
print(historiales["juan"].get())
navegar_adelante(historiales, "juan")
print(historiales["juan"].get())"""


###############EJ 23

inventario = {}

#1

def agregar_producto(inventario:dict,nombre:str,precio:int,cantidad:int):
        info = {}
        inventario[nombre] = info
        info["precio"] = precio
        info["cantidad"] = cantidad

agregar_producto(inventario, "jean", 20, 1)
# print(inventario)
agregar_producto(inventario,"remera",10, 40)
# print(inventario)

#2

def actualizar_stock(inventario:dict, nombre:str, cantidad:int):
    inventario[nombre]["cantidad"] = cantidad

actualizar_stock(inventario, "jean", 15)
# print(inventario)

#3

def actualizar_precio(inventario:dict, nombre:str, precio:int):
    inventario[nombre]["precio"] = precio

actualizar_precio(inventario, "jean", 100)
# print(inventario)

#4

def calcular_valor_inventario(inventario)->int:
    res:int = 0
    for key in inventario:
        termino:int = inventario[key]["precio"]*inventario[key]["cantidad"]
        res += termino
    
    return res

# print(calcular_valor_inventario(inventario))


####EXTRAS:

def lista_ordenada(s:list)->list:
    res: list = []
    t = s.copy()
    i: int = 0
    while i<(len(s)):
        res.append(menor(t))
        t[pos(t,menor(t))] = 10000000000000
        i +=1
    return res

def menor(s:list)->int:
    res = s[0]
    for i in range(len(s)):
        if s[i]<res:
            res = s[i]
    
    return res

def pos(s:list, x:int)->int:
    res:int = None
    for i in range(len(s)):
        if x == s[i]:
            res = i
    return res

# print(menor([10,2,3,4,5]))
# print(pos([10,2,3,4,5], menor([10,2,3,4,5])))
# print(lista_ordenada([2,5,1,3,4]))


def obtener_maxima_key1(d:dict)->str:
    res: int = None
    maximo: int = 0
    for key in d:
        if d[key] > maximo:
            res = key
            maximo = d[key]
    
    return res

# ejemplo = {"h":10,"a":2,"c":3,"d":100}
# print(obtener_maxima_key1(ejemplo))

def pertenece (x:int,s:list)->bool:
    res: bool = False
    
    for i in range (len(s)):
        if s[i]==x:
            res = True
            
    return res

# print(pertenece(2,[1,2,3]))

def ver(s:list)->list:
    res = []
    res.append(s[1])
    return res

# s = [1,2,63]
# ver(s)
# print(s)


def porcentaje (cien, cuanto)->float:
    res = (cuanto*100)/cien
    print (f'porcentaje ={res}%')
    print(f'diferencia = {res-100}%')
    return res

# porcentaje(100,20)
porcentaje(2000,307)  
porcentaje(3000,97)
porcentaje(300,7)
porcentaje(50,0)
# porcentaje(0,50)