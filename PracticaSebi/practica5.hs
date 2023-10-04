{--
FUNCIONES:
l = [0, 1, 2, 3]
head (l)= 0
tail(l) = [1, 2]
0:[1,2,3] = [0,1,2,3]
[1,2,3] ++ 0 = [1,2,3, 0]
--}

------EJ 1--------

--1
longitud :: [t] -> Integer
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--2
{--
problema ultimo (s: seq⟨T⟩) : T {
requiere: { |s| > 0 }
asegura: { resultado = s[|s| − 1] }
}
--}

ultimo :: [t] -> t 
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--3
{--
problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { |s| > 0 }
asegura: { resultado = subseq(s, 0, |s| − 1) }
}
--}

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

--4
{--
problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
requiere: { T rue }
asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
}
--}

reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

------EJ 2--------

--1
{--
problema pertenece (e: T, s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ e ∈ s }
}
--}

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs)  | n==x = True
                    | otherwise = pertenece n xs

--2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [x] = True
todosIguales (x:y:xs) | x == y = todosIguales (y:xs)
                      | x /= y = False

--3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:y:xs) | x /= y = todosDistintos (x:xs) && todosDistintos (y:xs)
                        | x == y = False

--4

{--
problema hayRepetidosF (s: seq⟨T ⟩) : B {
requiere: { T rue }
asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
}
--}

hayRepetidos :: Eq(t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:y:xs) | x==y = True
                      | otherwise = hayRepetidos (x:xs) 

hayRepetidosF :: Eq(t) => [t] -> Bool
hayRepetidosF [] = False
hayRepetidosF [x] = False
hayRepetidosF (x:y:xs) = hayRepetidos (x:y:xs) || hayRepetidosF (y:xs) 

--5
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs

--6
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs

--7
{--
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos  [] = []
eliminarRepetidos  (x:y:xs) = x : eliminarRepetidos  (quitarTodos x (x:y:xs))
--}

eliminarRepetidos1 :: (Eq t) => [t] -> [t]
eliminarRepetidos1  [] = []
eliminarRepetidos1 s = head s : eliminarRepetidos1  (quitarTodos (head s) s)

--8 

ida :: (Eq t) => [t] -> [t] -> Bool
ida [] _ = True
ida v s = pertenece (head v) s && ida (tail v) s

mismosElementos1 :: (Eq t) => [t] -> [t] -> Bool
mismosElementos1 v s = ida v s && ida s v

 --9
 {--
 problema capicua (s: seq⟨T⟩) : B {
requiere: { T rue }
asegura: { (resultado = true) ↔ (s = reverso(s)) }
}
 --}

capicua :: (Eq t) => [t] -> Bool
capicua s | reverso s == s = True 
          | otherwise = False  

--------EJ 3-------

--1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x:xs) = x * productoria xs 

--3
{--
problema maximo (s: seq⟨Z⟩) : Z {
requiere: { |s| > 0 }
asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
}
--}

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:y:xs) | y <= x = maximo (x:xs)
                | otherwise = maximo (y:xs)

--4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (n+x) : sumarN n xs

--5
sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

--6
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo s = sumarN (ultimo s) s

--7
pares  :: [Integer] -> [Integer]
pares [] = []
pares (x:xs) | x `mod` 2 == 0 = x : pares xs
             | otherwise = pares xs

--8
multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN n [] = []
multiplosDeN n (x:xs) | x `mod` n == 0 = x : multiplosDeN n xs
                    | otherwise = multiplosDeN n xs

--9 
--sin tener en cuenta repetidos
sacaN :: Integer -> [Integer] -> [Integer]
sacaN n [] = []
sacaN n (x:xs) | n == x = sacaN n xs
               | otherwise = x : sacaN n xs
               
ordenar :: [Integer] -> [Integer]
ordenar [y] = [y]
ordenar (x:xs) = ordenar (sacaN (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]

---teniendo en cuenta repetidos
sacaN2 :: Integer -> [Integer] -> [Integer]
sacaN2 n [] = []
sacaN2 n (x:xs) | n == x = xs
                | otherwise = x : sacaN2 n xs
               
ordenar2 :: [Integer] -> [Integer]
ordenar2 [y] = [y]
ordenar2 (x:xs) = ordenar2 (sacaN2 (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]

---------EJ 4---------

--1
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [' '] = [' ']
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs) | x == y && x == ' ' = sacarBlancosRepetidos (x:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs) 

--2

contarPalabras :: [Char] -> Integer
contarPalabras (x:xs) = contarEspacios (sacarEspaciosIniFin(x:xs)) + 1


sacarEspaciosIniFin :: [Char] -> [Char]
sacarEspaciosIniFin (x:xs) | head (sacarBlancosRepetidos(x:xs)) == ' ' && ultimo (sacarBlancosRepetidos(x:xs)) == ' ' =
                             tail (quitarUltimo (sacarBlancosRepetidos(x:xs)))
                           | head (sacarBlancosRepetidos(x:xs)) == ' ' =  tail (sacarBlancosRepetidos(x:xs))
                           | ultimo (sacarBlancosRepetidos(x:xs)) == ' ' = quitarUltimo (sacarBlancosRepetidos(x:xs))
                           | otherwise = (x:xs)

quitarUltimo :: [Char] -> [Char]
quitarUltimo [x] = []
quitarUltimo (x:xs) = x : quitarUltimo xs

contarEspacios :: [Char] -> Integer
contarEspacios [] = 0
contarEspacios (x:xs) | x == ' ' = 1 + contarEspacios xs
                      | otherwise = contarEspacios xs

---3 

palabras :: [Char] -> [[Char]]
palabras x = armarLista (sacarEspaciosIniFin x)

armarLista :: [Char] -> [[Char]]
armarLista [] = []
armarLista xs = [primerPalabra xs] ++ armarLista (sacarPrefijo (primerPalabra xs) xs)


primerPalabra :: [Char] -> [Char]
primerPalabra [] = []
primerPalabra (x:xs) | x /= ' ' = x : primerPalabra xs
                     | x == ' ' = []

sacarPrefijo :: [Char] -> [Char] -> [Char]
sacarPrefijo [] [] = []
sacarPrefijo [] (y:ys) | y == ' ' = ys
                       |otherwise = (y:ys)
sacarPrefijo (x:xs) (y:ys) | x == y = sacarPrefijo xs ys
                           | y == ' ' = ys
                           | otherwise = ys

---4

palabraMasLarga  :: [Char] -> [Char]
palabraMasLarga v = compararCadenaDePalabras (primerPalabra (sacarEspaciosIniFin v)) 
                    (sacarPrefijo (primerPalabra (sacarEspaciosIniFin v)) (sacarEspaciosIniFin v))

contarCaracteres :: [Char] -> Integer
contarCaracteres [] = 0
contarCaracteres (x:xs) = 1 + contarCaracteres xs

compararPalabras :: [Char] -> [Char] -> [Char]
compararPalabras x s | contarCaracteres x <= contarCaracteres s = s   
                     | otherwise = x


compararCadenaDePalabras :: [Char] -> [Char] -> [Char]
compararCadenaDePalabras (x:xs) [] = (x:xs)
compararCadenaDePalabras (x:xs) (y:ys) | compararPalabras (x:xs) (primerPalabra (y:ys) ) ==  (x:xs) 
                                         = compararCadenaDePalabras (x:xs) (sacarPrefijo (primerPalabra (y:ys)) (y:ys))
                                       | otherwise = compararCadenaDePalabras (primerPalabra(y:ys)) (sacarPrefijo (primerPalabra (y:ys)) (y:ys))
                                         
test1 = palabraMasLarga "esto es boca juniors" == "juniors"
test2 = palabraMasLarga "  me llamo sebastian" == "sebastian"
test3 = palabraMasLarga "hola     soy estudiante" == "estudiante"

---5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar v = head v ++ aplanar (tail v)

---6
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos v = head v ++ " "  ++ aplanarConBlancos (tail v)

---7

aplanarConNBlancos :: Integer -> [[Char]] -> [Char]
aplanarConNBlancos _ [] = []
aplanarConNBlancos _ [x] = x
aplanarConNBlancos n v = head v ++ insertarNBlancos n  ++ aplanarConNBlancos n (tail v)


insertarNBlancos :: Integer -> [Char]
insertarNBlancos n | n == 1 = " "
                   | otherwise = " " ++ insertarNBlancos (n-1)

-----

pertenecex :: Integer -> [Integer] -> Bool
pertenecex _ [] = False
pertenecex n (x:xs) | n == x = True
                   | otherwise = pertenecex n xs


contenidox :: [Integer] -> [Integer] -> Bool
contenidox [] _ = True
contenidox _ [] = False
contenidox (x:xs) (y:ys) = pertenecex x (y:ys) && contenidox xs (y:ys)

mismosElem :: [Integer] -> [Integer] -> Bool
mismosElem x v = contenidox x v && contenidox v x

sacarPalabra :: String -> [String] -> [String]
sacarPalabra _ [] = []
sacarPalabra v (x:xs) | v == x = sacarPalabra v xs
                      | otherwise = x : sacarPalabra v xs

sacarPalabrasRep :: [String] -> [String]
sacarPalabrasRep [] = []
sacarPalabrasRep [x,y] | x == y =[x]
                       | otherwise = [x,y]
sacarPalabrasRep (x:y:xs) = x : sacarPalabrasRep (sacarPalabra x (x:y:xs))

------EJ 5

--a

sumaAcumulada :: (Num t) => [t] -> [t] 
sumaAcumulada [] = []
sumaAcumulada v = sumaAcumulada (sacarUltimoElemento v) ++ [sumaDeTodos v]

--al pedo--
sumaAcumuladaHasta :: (Num t,Eq t) => t -> [t] -> t
sumaAcumuladaHasta n [] = 0
sumaAcumuladaHasta n (x:xs) | n == x = n
                            | otherwise = x + sumaAcumuladaHasta n xs
-----------

sumaDeTodos :: (Num t) => [t] -> t 
sumaDeTodos [] = 0
sumaDeTodos (x:xs) = x + sumaDeTodos xs

sacarUltimoElemento :: (Num t) => [t] -> [t]
sacarUltimoElemento [x] = []
sacarUltimoElemento (x:xs) = x : sacarUltimoElemento xs

--b

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = descomponerEnPrimosIndi x : descomponerEnPrimos xs


esPrimoAux :: Integer -> Integer -> Bool
esPrimoAux 1 _ = False
esPrimoAux _ 1 = True
esPrimoAux n i | n `mod` i /= 0 = esPrimoAux n (i-1)
               | otherwise = False

esPrimo :: Integer -> Bool
esPrimo n = esPrimoAux n (n-1)


descomponerEnPrimosIndiAux :: Integer -> Integer -> [Integer]
descomponerEnPrimosIndiAux _ 1 = []
descomponerEnPrimosIndiAux i n | esPrimo i && n `mod` i == 0 = i : descomponerEnPrimosIndiAux (i) (n `div` i)
                               | otherwise = descomponerEnPrimosIndiAux (i+1) n

descomponerEnPrimosIndi :: Integer -> [Integer]
descomponerEnPrimosIndi n = descomponerEnPrimosIndiAux 2 n

-------palabras

palabrasx :: [Char] -> [[Char]]
palabrasx [] = []
palabrasx v = primerPalabrax (sacarEspaciosIniFin v) : palabrasx (sacarPrefijox (primerPalabrax (sacarEspaciosIniFin v)) (sacarEspaciosIniFin v))


primerPalabrax :: [Char] -> [Char]
primerPalabrax [] = []
primerPalabrax (x:xs) | x == ' ' = []
                      | otherwise = x : primerPalabrax xs
  
sacarPrefijox :: [Char] -> [Char] -> [Char]
sacarPrefijox (x:xs) (y:ys) | x == y = sacarPrefijox xs ys
                            | otherwise = (y:ys)
sacarPrefijox [] (y:ys) | y == ' ' = ys
                        | otherwise = (y:ys)
sacarPrefijox [] [] = []

-------palabraMasLarga
palabraMasLargax :: [Char] -> [Char]
palabraMasLargax v = elementoMasLargo (palabrasx v)

elementoMasLargo :: [[Char]] -> [Char]
elementoMasLargo [x] = x
elementoMasLargo (x:y:xs) | length x > length y = elementoMasLargo (x:xs)
                          | otherwise = elementoMasLargo (y:xs)


----------------
sacarBlancosRepetidosx :: [Char] -> [Char]
sacarBlancosRepetidosx [x] = [x]
sacarBlancosRepetidosx (x:y:xs) | x == y && x == ' ' = sacarBlancosRepetidosx (x:xs)
                                | otherwise = x : sacarBlancosRepetidosx (y:xs)
----------------

contarPalabrasx :: [Char] -> Integer
contarPalabrasx v = contarEspaciosx v + 1


ultimoElem :: [Char] -> Char
ultimoElem [x] = x
ultimoElem (x:xs) = ultimoElem xs

sacarUltimo :: [Char] -> [Char]
sacarUltimo [] = []
sacarUltimo [x] = []
sacarUltimo (x:xs) = x : sacarUltimo xs

sacarEspaciosIniFinx :: [Char] -> [Char]
sacarEspaciosIniFinx [] = []
sacarEspaciosIniFinx (x:xs) | x == ' ' && ultimoElem (x:xs) == ' ' = sacarEspaciosIniFinx (sacarUltimo xs)
                            | x == ' ' = sacarEspaciosIniFinx xs
                            | ultimoElem (x:xs) == ' ' = sacarEspaciosIniFinx (sacarUltimo (x:xs))
                            | otherwise = (x:xs)

contarEspaciosx :: [Char] -> Integer
contarEspaciosx [] = 0
contarEspaciosx (x:xs) | x == ' ' = 1 + contarEspaciosx xs
                       | otherwise = contarEspaciosx xs


                       