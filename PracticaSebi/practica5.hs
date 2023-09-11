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

------EJ 2--------

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