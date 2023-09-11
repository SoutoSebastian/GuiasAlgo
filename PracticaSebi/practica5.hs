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
                       

--------EJ 3-------
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