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

---------------EJ 7----------------
todosDigitosIguales