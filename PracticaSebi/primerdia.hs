doubleMe :: Int ->Int
doubleMe x = x+x

--------------EJ 1-------------

--a
f :: Int -> Int
f x |x==1 =8
    |x==4 =131
    |x==16 =16

--b
g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

--c 
--gof
k :: Int -> Int
k x |x==1 = g(f 1)
    |x==4 = g(f 4)
    |x==16 = g(f 16)

--fog
h :: Int -> Int
h x |x==8 = f(g 8)
    |x==16 = f(g 16)
    |x==131 = f(g 131)

------------EJ 2-----------

--a 
-- problema absoluto (n:Z) :Z {
      --requiere {True}
      --asegura { res es el valor absoluto de n }
--}

absoluto :: Int -> Int
absoluto x |x>0 =x
           |x==0 = 0
           |x<0 =(-1)*x

--b
-- problema maximoabsoluto (y:Z, x:Z) :Z {
      --requiere {True}
      --asegura { res es el maximo entre el valor absoluto de x e y }
--}

maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y|absoluto(x)<absoluto(y) =absoluto(y)
                  |absoluto(x)>absoluto(y) =absoluto(x)
                  |otherwise = absoluto(x)

--c 
-- problema maximo3 (y:Z, x:Z, z:Z) :Z {
      --requiere {True}
      --asegura { res es el maximo entre el valor absoluto de x, y, z }
--}

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x>=y && x>=z =x
              | y>=x && y>=z =y
              | z>=x && z>=y =z

--d
-- problema algunoEs0 (y:R, x:R) :Bool {
      --requiere {True}
      --asegura { res devuelve true si uno de los dos datos de entrada es igual a 0 }
      --asegura {res devuelve false si ninguno de los datos de entrada es igual a 0}
--}

algunoEs0 :: Int -> Int -> Bool
algunoEs0 y x |x==0 || y==0 =True
              |otherwise =False

algunaEs01 :: Int -> Int -> Bool
algunaEs01 0 _ = True
algunaEs01 _ 0 = True
algunaEs01 x y = False

--e
-- problema ambosSon0 (y:R, x:R) :Bool {
      --requiere {True}
      --asegura { res devuelve true si uno de los dos datos de entrada es igual a 0 }
      --asegura {res devuelve false si no se cumple que los dos datos de entrada son iguales a 0}
--}

ambosSon0 :: Int -> Int -> Bool
ambosSon0 0 0 = True
ambosSon0 _ _ = False

ambosSon01 :: Int -> Int -> Bool
ambosSon01 x y |x==0 && y==0 = True
               |otherwise = False

--f
-- problema mismoIntervalo (y:R, x:R) :Bool {
      --requiere {True}
      --asegura {res devuelve True si x e y pertencen ambos a los intervalos (-inf, 3] o (3, 7] o (7, +inf)
      --asegura {res devuelve False si x e y no pertencen al mismo intervalo}
--}

mismoIntervalo :: Int -> Int -> Bool
mismoIntervalo x y |x<=3 && y<3 = True
                   |x>3 && x<=7 && y>3 && y<=7 = True
                   |x>7 && y>7 = True
                   |otherwise = False

--g
-- problema sumaDistintos (y:R, x:R, z:R) :R {
      --requiere {True}
      --asegura {res devuelve la sume de los tres números ingresados sin sumar repetidos}
--}

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x/=y && x/=z && y/=z = x+y+z
                    |x==y && x/=z = x+z
                    |x/=y && x==z = x+y
                    |x/=y && x/=z && z==y = x+y
                    |x==y && x==z = x

--h
-- problema esMultiplode (y:R, x:R) :Bool {
      --requiere {True}
      --asegura {res devuelve True si x es multiplo de y}
      --asegura {res devuelve False si x no es multiplo de y}
--}

esMultiplode :: Int -> Int -> Bool
esMultiplode x y | mod x y == 0 = True
                 | otherwise = False


--I
-- problema digitoUnidades (y:Z) :Z {
      --requiere {True}
      --asegura {res es el digito de las unidades de y}
--}

digitoUnidades :: Int -> Int
digitoUnidades y = mod y 10

--J
-- problema digitoDecenas (y:Z) :Z {
      --requiere {True}
      --asegura {res es el digito de las decenas de y}
--}

digitoDecenas :: Int -> Int
digitoDecenas y = div (mod y 100) 10 

---------EJ 3------------------

--problema estanRelacionados (x:Z, y:Z) : Bool {
      --requiere: {x /= 0 ∧ y /= 0}
      --asegura: {(res = true) ↔ x ∗ x + x ∗ y ∗ k = 0 para algun k ∈ Z con k /= 0)}
--}

estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | mod (x^2) (x*y) == 0 = True
                      | otherwise = False


-----------EJ 4--------------------

--a
--problema  prodInt (v:(RxR), w:(RxR)) : (RxR) {
      --requiere: {True}
      --asegura: {(res es el producto interno entre los dos tuplas}
--}

prodInt :: (Float, Float) -> (Float, Float) -> (Float, Float)
prodInt v w = ((fst v)*(fst w), (snd v)*(snd w))

--b
--problema  todoMenor (v:(RxR), w:(RxR)) : Bool {
      --requiere: {True}
      --asegura: {res devuelve True si cada coordenada de la primer tupla es menor que la coordenada
               --  correspondiente de la segunda tupla}
      --asegura: { res devuelve False si alguna coordenada de la primer tupla es mayor que la coordenada
               --  correspondiente de la segunda tupla}
--}

todoMenor :: (Float, Float) -> (Float,Float) -> Bool
todoMenor v w = (fst v)<(fst w) && (snd v)<(snd w)

--c
--problema distanciaPuntos (v:(RxR), w:(RxR)) : R {
      --requiere: {True}
      --asegura: {res devuelve la distancia entre ambos puntos}

--}

distanciaPuntos :: (Float, Float) -> (Float,Float) -> Float
distanciaPuntos v w = sqrt (((fst v) - (fst w))^2 + ((snd v) - (snd w))^2) 

--d
--problema sumaTerna (v:(ZxZxZ) : Z {
      --requiere: {True}
      --asegura: {res devuelve la suma de los elementos de la terna de enteros}

--}

sumaTerna :: (Integer, Integer, Integer) -> Integer   
sumaTerna (a, b, c) = a + b + c

--e
--problema sumarSoloMultiplos (v:(ZxZxZ), x:N) : Z {
      --requiere: {True}
      --asegura: {res devuelve la suma de los elementos de la terna que son multiplos de x}
--}

sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a, b, c) x | a `mod` x == 0 && b `mod` x == 0 && c `mod` x == 0 = a + b + c
                               | a `mod` x == 0 && b `mod` x == 0  = a + b
                               | a `mod` x == 0 && c `mod` x == 0 = a + c 
                               | b `mod` x == 0 && c `mod` x == 0 = b + c
                               | a `mod` x == 0 = a 
                               | b `mod` x == 0 = b 
                               | c `mod` x == 0 = c 
                               | otherwise = 0

--f 
--problema posPrimerPar (v:(ZxZxZ), x:N) : Z {
      --requiere: {True}
      --asegura: {res devuelve la posicion del primer numero par}
      --asegura: {res devuelve 4 si son todos impares}
--}

posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a, b, c) | a `mod` 2 == 0 = 1
                       | b `mod` 2 == 0 = 2
                       | c `mod` 2 == 0 = 3
                       | otherwise = 4 

--g
--problema crearPar (x:t1, y:t2) : (t1, t2)  {
      --requiere: {True}
      --asegura: {res devuelve una dupla a partir de x e y}
--}                               

crearPar :: t1 -> t2 -> (t1, t2)
crearPar x y = (x, y)

--h
--problema invertir (x:(t1, t2)) : (t2, t1) {
      --requiere: {True}
      --asegura: {res devuelve una dupla con el orden invertido}
--}

invertir :: (t1, t2) -> (t2, t1)
invertir (x, y) = (y,x)

-------------EJ 5--------------
{--
problema todosMenores ((n1,n2,n3) : Z × Z × Z) : Bool {
requiere: {T rue}
asegura: {(res = true) ↔ ((f(n1) > g(n1)) ∧ (f(n2) > g(n2)) ∧ (f(n3) > g(n3))))}
}
problema f (n: Z) : Z {
requiere: {T rue}
asegura: {(n ≤ 7 → res = n
2
) ∧ (n > 7 → res = 2n − 1)}
}
problema g (n: Z) : Z {
requiere: {T rue}
asegura: {Si n es un n´umero par, entonces res = n/2, en caso contrario, res = 3n + 1}
--}

f5 :: Integer -> Integer
f5 n | n <= 7 = n 
     | n > 7 = (2*n) -1

g5 :: Integer -> Integer
g5 n | n `mod` 2 == 0 = (n `div` 2)
     | otherwise = (3*n) + 1 

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (n1, n2, n3) = (f5 n1 > g5 n1) && (f5 n2 > g5 n2) && (f5 n3 > g5 n3)