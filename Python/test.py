
import math

####while
######## i: int = 0
######## while i < 5:, al final i = i +1

####for
#####for i in range(0,5,1)= range(5):


######EJ 1
#1
def boca():
    print ("boca juniors")

#2
def imprimir_un_verso():
    print ("Muchos truco como Tony Hawk\nMucho invento como Tony Stark")

imprimir_un_verso()

#3
def raiz_de_2():
    res: float = round((math.sqrt(2)), 4)
    print(res)


raiz_de_2()


#4 
def factorial_2():
    print("2")


#5
def perimetro()->int:
    res: int = 2*math.pi 
    return res

print(perimetro())


######EJ 2

#1
def imprimir_saludo (nombre:str):
    print ("Hola " + str(nombre))

imprimir_saludo("juan")

#2
def raiz_cuadrada_de(numero: int)-> float:
    res: float = math.sqrt(numero)
    return res


#3
def farenheit_a_celcius(t:float)-> float:
    res: float = ((t-32)*5)/9
    return res


#4
def imprimir_dos_veces(e:str)-> str:
    print (e*2)

#5
def es_multiplo_de(n: int,m: int)->bool:
    res:bool = n%m == 0
    return res

#6
def es_par(n:int)->bool:
    res: bool = es_multiplo_de(n,2)
    return res


#7
def cantidad_de_pizzas(comensales: int, minp: int)->int:
    res: int = int((minp/8)*comensales+0.9)
    return res

#####EJ 3

#1
def alguno_es_0(n: int, m:int)->bool:
    res: bool = (n==0 or m==0)
    return res


#3
def es_nombre_largo(nombre:str)->bool:
    l: int = len(nombre)
    res: bool = (3<=l) and (l<=8)
    return res


#####EJ 5

#1
def devolver_el_doble_si_es_par(x: int):
    d: int = x
    if (x%2 == 0):
        d = 2*x
    return d


#####EJ 6
#2
def hasta_40 ():
    i=10
    while (i<41):
        if (es_par(i)==True):
            print(i)
        i = i +1

#####EJ 7

#2
def hasta_40for():
    for i in range (10,41,2):
        print(i)
        i=i+1



test1 = es_multiplo_de(10,5)
print("el resultado de es_multiplo_de(10,5):" ,test1)
test2 = es_nombre_largo("sjdsdjsjjsssss")
print(test2)
test3 = es_nombre_largo("sss")
print(test3)
test4 = devolver_el_doble_si_es_par(2)
print(test4)
test5 = devolver_el_doble_si_es_par(5)
print(test5)
test6 = raiz_cuadrada_de(16)
print (test6)
test7 = farenheit_a_celcius (20)
print (test7)
test8 = cantidad_de_pizzas(2,10)
print (test8)
hasta_40for()
test9 = alguno_es_0(0,1)
print(test9)
test10 = alguno_es_0(2,1)
print(test10)