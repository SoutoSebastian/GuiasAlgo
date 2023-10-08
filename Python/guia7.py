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
def pertenece(s:list, e:int)->bool:
    for i in range (len(s)):
        if(s[i] == e):
            res:bool = True
            break
        else:
            res :bool =False
            
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

def sumaTotal (s:list)->int:
    suma = 0
    for i in s:
        suma += i
    return suma
        
# test7 = sumaTotal([1,2,3])
# print(test7)


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

test8 = ordenados([1,2,3])
print(test8)
print(ordenados([2,1,5]))
print(ordenados([1,2,3,4,5,6,4]))