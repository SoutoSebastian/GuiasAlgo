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
sacaN :: Integer -> [Integer] -> [Integer]
sacaN n [] = []
sacaN n (x:xs) | n == x = sacaN n xs
               | otherwise = x : sacaN n xs
               
ordenar :: [Integer] -> [Integer]
ordenar [y] = [y]
ordenar (x:xs) = ordenar (sacaN (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]