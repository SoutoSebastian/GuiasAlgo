
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

#imprimir_un_verso()

#3
def raiz_de_2():
    res: float = round((math.sqrt(2)), 4)
    print(res)


#raiz_de_2()


#4 
def factorial_2():
    print("2")


#5
def perimetro()->int:
    res: int = 2*math.pi 
    return res

#print(perimetro())


######EJ 2

#1
def imprimir_saludo (nombre:str):
    print ("Hola " + str(nombre))

#imprimir_saludo("juan")

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


#2
def ambos_son_0(n:int, m:int)->bool:
    res: bool = (n==0 and m==0)
    return res


#3
def es_nombre_largo(nombre:str)->bool:
    l: int = len(nombre)
    res: bool = (3<=l) and (l<=8)
    return res

#4
def es_bisiesto(año:int)->bool:
    res: bool = (año%400==0)
    return res

#####EJ 4

#1
def peso_pino(altura: int)-> int:
    if (altura<=3):
        res: int = altura*300
    else:
        res: int = 3*300+(altura - 3) * 200
    return res


#2
def es_peso_util(x:int)->bool:
    res: bool = 400<=x and x<=1000
    return res

#4
def sirve_pino(altura:int)->bool:
    res :bool = es_peso_util(peso_pino(altura))
    return res

#3
def sirve_pino_rustica(altura:int)->bool:
    if (altura<=3):
        res: bool = 400<=(altura*300)<=1000
    else:
        res: bool = 400<=(3*300+(altura - 3) * 200)<=1000
    return res

#####EJ 5


#1
def devolver_el_doble_si_es_par(x: int):
    d: int = x
    if (x%2 == 0):
        d = 2*x
    return d


#2
def devolver_valor_si_es_par_sino_el_que_sigue(x: int)->int:
    if (x%2==0):
        res=x
    else:
        res=x+1
    return res


#3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(x:int)->int:
    if (x%9==0):
        res=x*3
    elif (x%3==0):
        res=x*2
    else:
        res=x
    return res


#4
def lindo_nombre(nombre:str)->str:
    if (len(nombre)>=5):
        res = "Tu nombre tiene muchas letras!"
    else:
        res = "Tu nombre tiene menos de 5 caracteres"
    return res


#5
def elRango(x:int)->str:
    if (x<5):
        print ("Menor a 5")
    elif (10<=x<=20):
        print ("Entre 10 y 20")
    else:
        print("Mayor a 20")


#6
def a_laburar(s:str,y:int)->str:
    if (y<=18):
        print ("Andá de vacaciones")
    elif (s=="F" and y>=60):
        print("Andá de vaciones")
    elif (s=="M" and y>=65):
        print("Andá de vaciones")
    else:
        print("Te toca trabajar")


#####EJ 6


#1
def al_10 ():
    i=1
    while (i<11):
        print (i)
        i = i + 1


#2
def hasta_40 ():
    i=10
    while (i<41):
        if (es_par(i)==True):
            print(i)
        i = i +1


#3
def eco():
    i=1
    while (i<11):
        print ("eco")
        i = i + 1
        

#4
def despegue(i:int):
    while (i>=1):
        print(i)
        i = i - 1
    print("Despegue!")


#5
def viaje_en_el_tiempo(a:int, a2:int):
    while (a>a2):
        print("Viajó un año al pasado, estamos en el año:" + str(a-1))
        a = a - 1
    print("Viajó un año al pasado, estamos en el año:" + str(a2))


#6
def aristoteles_viaje (a:int):
    while (a-20>(-384)):
        if ((a-20)>=0):
            print("Viajó 20 años al pasado, estamos en el año:" + str(a-20))
        else:
            print("Viajó 20 años al pasado, estamos en el año:" + str ((a-20)*(-1)) + "a.C")
        a = a-20


#####EJ 7


#1
def al_10for ():
    for i in range (1,11,1):
        print(i)
#        i = i + 1
    

#2
def hasta_40for():
    for i in range (10,41,2):
        print(i)
#        i=i+1


#3
def eco_for():
    for i in range (1,11,1):
        print("eco")
 #       i = i + 1


#4 
def despegue_for(i:int):
    for i in range (i,0,(-1)):
        print(i)
    print("Despegue!")


#5
def viaje_en_el_tiempo_for (a:int, a2:int):
    for a in range (a,a2,-1):
        print ("Viajó un año al pasado, estamos en el año:" + str(a-1))
        
    print("Viajó un año al pasado, estamos en el año:" + str(a2))


#6
def aristoteles_viaje_for (a:int):
    for a in range (a,-384,-20):
        if ((a-20)>=0):
            print("Viajó 20 años al pasado, estamos en el año:" + str(a-20))
        else:
            print("Viajó 20 años al pasado, estamos en el año:" + str ((a-20)*(-1)) + "a.C")


#####EJ 8 (estados)

#1
# x@a=5, y@a=7

#2
# x@a=5, y@a=7, z@a=12, y@b=24

#3
# x@a=5, y@a=7, x@b="hora", y@b="horahora"

#4
# x@a=False, res@a=True

#5
# x@a=True, y@a=False, res@a=False, x@b=False


#####EJ 9
#1
# x + g = 4

#2
# x + g = 2

#3
def rt(x: int, g: int) -> int:
    #estado a
    g = g + 1 #estado b: g@b = g@a + 1
    return x + g # = x@a + g@b

g: int = 0 # estado a, g@a = 0
def ro(x: int) -> int: # estado b
    global g
    g = g + 1 #estado c: g@c = g@a + 1
    return x + g # = x@b + g@c


#4
#ESPECIFICACIONES

# problema rt (in x:Z, in g:Z) :Z {
#   requiere :{True}
#   asegura : {res = (g+1) + x)}
#}


# problema ro (in x:Z) :Z {
#   requiere :{True}
#   asegura : {res = (g@a+1) + x)}
#}


#test1 = es_multiplo_de(10,5)
#print("el resultado de es_multiplo_de(10,5):" ,test1)
#test2 = es_nombre_largo("sjdsdjsjjsssss")
##print(test2)
#test3 = es_nombre_largo("sss")
#print(test3)
#test4 = devolver_el_doble_si_es_par(2)
#print(test4)
#test5 = devolver_el_doble_si_es_par(5)
#print(test5)
#test6 = raiz_cuadrada_de(16)
#print (test6)
#test7 = farenheit_a_celcius (20)
#print (test7)
#test8 = cantidad_de_pizzas(2,10)
#print (test8)
##hasta_40for()
#test9 = alguno_es_0(0,1)
#print(test9)
#test10 = alguno_es_0(2,1)
#print(test10)
#test11 = ambos_son_0(0,0)
#print(test11)
#test12 = ambos_son_0(1,0)
#print(test12)
#test13 = es_bisiesto(2000)
#print(test13)
#test14 = es_bisiesto(2023)
#print(test14)
#test15 = peso_pino(2)
#print(test15)
#test16 = peso_pino(5)
#print(test16)
#test17 = es_peso_util(500)
#print(test17)
#test18 = es_peso_util(2)
#print(test18)
#test19 = sirve_pino_rustica(2)
#print(test19)
#test20 = sirve_pino_rustica(5)
#print(test20)
#test21 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(3)
#print(test21)
#test22 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(27)
#print(test22)
#test23 = devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(5)
#print(test23)
#test24 = lindo_nombre("sebastian")
#print(test24)
#test25 = lindo_nombre("juan")
#print(test25)
#elRango(2)
#elRango(15)
#elRango(30)
#a_laburar("F", 70)
#a_laburar("F", 30)
#a_laburar("M", 70)
#a_laburar("M", 60)
#a_laburar("M", 10)
#al_10()
#eco()
#despegue(10)
#viaje_en_el_tiempo(2015,2010)
#aristoteles_viaje(100)
#al_10for()
#test26 = eco_for() == eco()
#print(test26)
#despegue_for(10)
#viaje_en_el_tiempo_for(2015, 2011)
#aristoteles_viaje_for(84)