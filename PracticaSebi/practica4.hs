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

---------------EJ 4----------------
sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = 1
              | n `mod` 2 /= 0 = n + sumaImpares (n-1)
              | n `mod` 2 == 0 = sumaImpares (n-1)

---------------EJ 5----------------
medioFact :: Integer -> Integer
medioFact n | n <=1 = 1
            | otherwise = n * medioFact (n-2)

---------------EJ 6----------------
sumaDigitos :: Integer -> Integer
sumaDigitos n | cantDigitos n == 1 = n
              | otherwise = ultimoDigito n + sumaDigitos (sacarUltimoDigito n)

---------------EJ 7----------------

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | n<10 = True
                      | otherwise= ultimoDigito n == anteultimoDigito n && todosDigitosIguales (sacarUltimoDigito n)

--funciones auxiliares

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

anteultimoDigito :: Integer -> Integer
anteultimoDigito n = div (mod n 100) 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div n 10

--------------EJ 8------------------
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | i == cantDigitos n = ultimoDigito n
                 | otherwise = iesimoDigito (sacarUltimoDigito n) i


cantDigitos :: Integer -> Integer
cantDigitos n | n<10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

--------------EJ 9------------------

esCapicua :: Integer -> Bool
esCapicua n | cantDigitos n == 1 = True
            | primerDigito n == ultimoDigito n = esCapicua (reducirNumero n)
            |otherwise = False

primerDigito :: Integer -> Integer
primerDigito n | n<10 = n
               | otherwise = n `div` 10^((cantDigitos n)-1)

sacarPrimerDigito :: Integer -> Integer
sacarPrimerDigito n = mod n (10^((cantDigitos n)-1))

reducirNumero :: Integer -> Integer
reducirNumero n = sacarPrimerDigito (sacarUltimoDigito n)
           

--------------EJ 10-----------------
--a
{--
problema f1a (n:Z) :Z {
    requiere: {True}
    asegura: {res = sumatoria de i=0 hasta n de 2^i}
}
--}

f1a :: Integer -> Integer
f1a n | n == 0 = 1
      | otherwise = 2^n + f1a (n-1)

--b 
{--
problema f2b (n:Z, q:R) :R {
    requiere: {True}
    asegura: {res = sumatoria de i=0 hasta n de q^i}
}
--}

f2b :: Integer -> Float -> Float
f2b n q | n == 0 = 1
        | otherwise = q^n + f2b (n-1) q

--c
{--
problema f3c (n:Z, q:R) :R {
    requiere: {True}
    asegura: {res = sumatoria de i=0 hasta 2n de q^i}
}
--}

f3b :: Integer -> Float -> Float
f3b n q = f2b (2^n) q

--d
{--
problema f4d (n:Z, q:R) :R {
    requiere: {True}
    asegura :{res = sumatoria de i=n hasta 2n de q^1}
}
--}

f4d :: Integer -> Float -> Float
f4d n q = f3b n q - f2b n q + q^n

--------------EJ 11----------
--a

eAprox :: Integer -> Float
eAprox n | n==0 = 1
         | otherwise = 1 / factorial n + eAprox (n-1)

factorial :: Integer -> Float
factorial n | n == 0 = 1
            | otherwise = fromIntegral n * (factorial (n-1))

--b 
e :: Float
e = eAprox 10

--------------EJ 12------------

sucesion12 :: Integer -> Float
sucesion12 n | n == 1 = 2
             | otherwise = 2 + (1/sucesion12 (n-1))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesion12 n - 1





