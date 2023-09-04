------------------EJ 1--------------
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            |otherwise = fibonacci (n-1) + fibonacci (n-2)

-----------------EJ 2----------------
parteEntera :: Float -> Integer
parteEntera x | 0<=x && x<1 = 0
              | x<0 = -1 + parteEntera (x+1)
              | otherwise = 1 + parteEntera (x-1)

---------------EJ 3------------------
esDivisible :: Integer -> Integer -> Bool
esDivisible x y | x == y = True
                | x<y = False
                | otherwise = esDivisible (x-y) y

---------------EJ 7----------------

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n<10 = True
                      | otherwise= primerDigito n == segundoDigito n && todosDigitosIguales (sacarPrimerDigito n)

--funciones auxiliares

primerDigito :: Integer -> Integer
primerDigito n = mod n 10

segundoDigito :: Integer -> Integer
segundoDigito n = div (mod n 100) 10

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n = div n 10

--------------EJ 8------------------
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = primerDigito n
                 | otherwise = iesimoDigito (sacarPrimerDigito n) i


cantDigitos :: Integer -> Integer
cantDigitos n | n<10 = 1
              | otherwise = 1 + cantDigitos (div n 10)