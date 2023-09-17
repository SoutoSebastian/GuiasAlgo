-------------ej
{--
problema relacionesValidas {relaciones : seq(String x String)} :Bool {
    requiere: {True}
    asegura: {(res = True) <-> no hay tuplas en relaciones con ambos componentes iguales en tuplas repetidas}
}
--}

componentesIguales :: ([Char], [Char]) -> Bool
componentesIguales (a,b) = a == b

mismaTupla :: ([Char],[Char]) -> ([Char],[Char]) -> Bool
mismaTupla x y = x == y

relacionesValidas :: [([Char] ,[Char])] -> Bool
relacionesValidas [x] = True
relacionesValidas (x:y:xs) | componentesIguales x && mismaTupla x y == True = False
                           | otherwise = relacionesValidas (x:xs) && relacionesValidas (y:xs)
