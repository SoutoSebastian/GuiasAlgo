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

------------EJ 13--------------
{--
problema dobleSumatoria (n:N, m:N) :R {
    requiere: {True}
    asegura: {res = doble sumatoria de i=1 hasta n y de j=1 hasta m de i^j}
}
--}

sumatoriaInterna :: Integer -> Integer -> Integer
sumatoriaInterna _ 0 = 0
sumatoriaInterna n m = n^m + sumatoriaInterna n (m-1)

dobleSumatoria :: Integer -> Integer -> Integer
dobleSumatoria 0 _ = 0
dobleSumatoria n m = sumatoriaInterna n m + dobleSumatoria (n-1) m

------------EJ 14----------------
{--
problema sumaPotencias (n:Z, q:N, m:N) :N {
    requiere: {True}
    asegura: {res = doble sumatoria de a=1 hasta n y de b=1 hasta m de q^(a+b)}
}
--}

sumatoriaPotencias1 :: Integer -> Integer -> Integer -> Integer
sumatoriaPotencias1 q n 1 = q^(n+1)
sumatoriaPotencias1 q n m = q^(n+m) + sumatoriaPotencias1 q n (m-1)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q 1 m = sumatoriaPotencias1 q 1 m
sumaPotencias q n m = sumatoriaPotencias1 q n m + sumaPotencias q (n-1) m

------------EJ 15---------------

{--
problema sumaRacionales (n : N, m : N) : R {
requiere: { T rue}
asegura: { resultado = doble sumatoria desde p=1 hasta n y q=1 hasta m de p/q}
}
--}

sumaRacionales1 :: Integer -> Integer -> Float
sumaRacionales1 n 1 = fromIntegral n 
sumaRacionales1 n m = (fromIntegral n)/(fromIntegral m) + sumaRacionales1 n (m-1) 

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 m = sumaRacionales1 1 m 
sumaRacionales n m = sumaRacionales1 n m + sumaRacionales (n-1) m 

-----------EJ 16-------------

--a
menorDivisorDesde :: Integer -> Integer-> Integer
menorDivisorDesde x y | x==y = y
                      | x `mod` y == 0 = y
                      |otherwise = menorDivisorDesde x (y+1)

menorDivisor :: Integer -> Integer
menorDivisor x | x == 1 = 1
               | otherwise = menorDivisorDesde x 2

--b
esPrimo :: Integer -> Bool
esPrimo x = menorDivisor x == x

--c
sonCoprimosv1 :: Integer -> Integer -> Integer -> Bool
sonCoprimosv1 x y z | z == 1 = True
                    | x `mod` z == 0 && y `mod` z == 0 = False                    
                    | otherwise = sonCoprimosv1 x y (z-1)

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos x y | x<=y = sonCoprimosv1 x y y
                | x>y = sonCoprimosv1 x y x

--d
quePrimoEs :: Integer -> Integer
quePrimoEs 2 = 1
quePrimoEs n | esPrimo n == True = 1 +quePrimoEs (n-1)
             | otherwise = quePrimoEs (n-1)

nEsimoPrimoAux :: Integer -> Integer -> Integer
nEsimoPrimoAux n i | quePrimoEs n == i = n 
                   |otherwise = nEsimoPrimoAux (n+1) i

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo i = nEsimoPrimoAux 2 i
-----------EJ 17----------
{--
problema esFibonacci (n: Z) : B {
requiere: { n ≥ 0 }
asegura: { resultado = true ↔ n es alg´un valor de la secuencia de Fibonacci definida en el ejercicio 1}
}
--}

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux _ (-1) = False
esFibonacciAux x n | x == fibonacci n = True
                   | otherwise = esFibonacciAux x (n-1)

esFibonacci :: Integer -> Bool
esFibonacci x = esFibonacciAux x 32

-----------EJ 18-----------
{--
problema mayorDigitoPar (n: N) : N {
requiere: { T rue }
asegura: { resultado es el mayor de los d´ıgitos pares de n. Si n no tiene ning´un d´ıgito par, entonces resultado es -1.
}
}
--}

esPar :: Integer -> Bool
esPar n = n `mod` 2 == 0

mayorDigitoParAux :: Integer -> Integer -> Integer
mayorDigitoParAux n y | n == 0 = y
                      | esPar (ultimoDigito n) && ultimoDigito n > y = mayorDigitoParAux (sacarUltimoDigito n) (ultimoDigito n)
                      | otherwise = mayorDigitoParAux (sacarUltimoDigito n) y

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = mayorDigitoParAux n (-1)

------------EJ 19------------
{--
problema esSumaInicialDePrimos (n: Z) : B {
requiere: { n ≥ 0 }
asegura: { resultado = true ↔ n es igual a la suma de los m primeros n´umeros primos, para alg´un m.}
}

--}

sumaDePrimosHasta :: Integer -> Integer 
sumaDePrimosHasta x | x == 2 = 2 
                    | esPrimo x = x + sumaDePrimosHasta (x-1)
                    | otherwise = sumaDePrimosHasta (x-1)


esSumaInicialDePrimosAux :: Integer -> Integer -> Bool
esSumaInicialDePrimosAux n m | n < sumaDePrimosHasta m = False
                             | n == sumaDePrimosHasta m = True
                             | otherwise = esSumaInicialDePrimosAux n (m+1)

esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 2 


------------EJ 20----------

{--
problema tomaValorMax (n1:Z, n2:Z) : Z {
    requiere: {n1>1 y n2>n1}
    asegura: {res es algun m tal que sumaDivisores(m) = max{sumaDivisores(i) | n1 ≤ i ≤ n2}
}
--}

sumaDivisoresAux :: Integer -> Integer -> Integer
sumaDivisoresAux n m | m == 1 = 1
                     | n `mod` m == 0 = m + sumaDivisoresAux n (m-1)
                     | otherwise = sumaDivisoresAux n (m-1)

sumaDivisores :: Integer -> Integer 
sumaDivisores n = sumaDivisoresAux n n

tomaValorMaxAux :: Integer -> Integer -> Integer -> Integer -> Integer
tomaValorMaxAux n1 n2 m q| n2 < q = m
                         | sumaDivisores m > sumaDivisores q = tomaValorMaxAux n1 n2 m (q+1)
                         | otherwise = tomaValorMaxAux n1 n2 q (q+1)

tomaValorMax :: Integer-> Integer -> Integer
tomaValorMax n1 n2 = tomaValorMaxAux n1 n2 n1 (n1+1)
 
 ---------EJ 21----------
 {--
 problema pitagoras (m:Z, n:Z, r:Z) :Z {
    requiere: {True}
    asegura: {res es la cantidad de pares (p, q) con 0 ≤ p ≤ m y 0 ≤ q ≤ n satisfacen que p^2 + q^2 ≤ r^2}
 --}

pitagorasAux :: Integer -> Integer -> Integer -> Integer
pitagorasAux m n r | n==0 && (m^2 + n^2 <= r^2) = 1
                   | n==0 && (r^2 < m^2 + n^2 ) = 0  
                   | (m^2 + n^2 <= r^2) = 1 + pitagorasAux m (n-1) r 
                   |  otherwise = pitagorasAux m (n-1) r 

pitagoras :: Integer -> Integer -> Integer -> Integer
pitagoras m n r | m==0 = pitagorasAux 0 n r 
                | otherwise = pitagorasAux m n r + pitagoras (m-1) n r  
