module Simulacro where 

fib :: Integer -> Integer
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) +fib (n-2)

----EJ 1
{--
problema relacionesValidas (relaciones: seq⟨String × String⟩) : Bool {
requiere: {True}
asegura: {(res = true) ↔ no hay tuplas en relaciones con ambas componentes iguales ni tuplas repetidas (sin considerar
el orden)}
}
--}

difTupla :: (String,String) -> (String,String) -> Bool
difTupla x v | fst x == fst v && snd x == snd v = False
             | fst x == snd v && snd x == fst v = False
             | otherwise = True

difElementos :: (String,String) -> Bool
difElementos x | fst x == snd x = False
               | otherwise = True

relacionesValidasAux :: [(String,String)] -> Bool
relacionesValidasAux [] = True
relacionesValidasAux [x] | difElementos x = True
                         | otherwise = False
relacionesValidasAux (x:y:xs) | difTupla x y && difElementos x = relacionesValidasAux (x:xs)
                              | otherwise = False

relacionesValidas :: [(String,String)] ->Bool
relacionesValidas [] = True
relacionesValidas [x] | difElementos x = True
                      | otherwise = False
relacionesValidas (x:y:xs) = relacionesValidasAux (x:y:xs) && relacionesValidas (y:xs)

--EJ 2

{--
problema personas (relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
  requiere: {relacionesValidas(relaciones)}
  asegura: {res no tiene elementos repetidos}
  asegura: {res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
}
--}

personasConRep :: [(String,String)] -> [String]
personasConRep [] = []
personasConRep [x] = fst x : snd x : []
personasConRep (x:y:xs) = fst x : snd x : personasConRep (y:xs)

sacarRepInicial :: String -> [String] -> [String]
sacarRepInicial _ [] = []
sacarRepInicial v (y:xs) | v == y = sacarRepInicial v xs
                         | otherwise = y : sacarRepInicial v xs

sacarRep :: [String] -> [String]
sacarRep (x:y:xs) = x : sacarRepInicial x (y:xs)


sacarTodosRep :: [String] -> [String]
sacarTodosRep [] = []
sacarTodosRep [x] = [x]
sacarTodosRep (x:xs) = x : sacarTodosRep (tail (sacarRep (x:xs)))


personas :: [(String,String)] -> [String]
personas [] = []
personas (x:xs) = sacarTodosRep (personasConRep (x:xs))

--EJ 3
{--
problema amigosDe (persona: String, relaciones: seq⟨String × String⟩) : seq⟨String⟩ {
requiere: {relacionesValidas(relaciones)}
asegura: {resu tiene exactamente los elementos que figuran en alguna tupla de relaciones en las que alguna de las
componentes es persona}
}
--}

amigosDeConPersona :: String -> [(String, String)] -> [String]
amigosDeConPersona _ [] = []
amigosDeConPersona t (x:xs) | fst x == t || snd x == t = fst x : snd x : amigosDeConPersona t xs
                            | otherwise = amigosDeConPersona t xs

amigosDe :: String -> [(String, String)] -> [String]
amigosDe _ [] = []
amigosDe t (x:xs) = sacarRepInicial t (amigosDeConPersona t (x:xs))

--EJ 4
{--
problema personaConMasAmigos (relaciones: seq⟨String × String⟩) : String {
requiere: {relaciones no vac´ıa}
requiere: {relacionesV alidas(relaciones)}
asegura: {resu es el Strings que aparece m´as veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
}
--}
