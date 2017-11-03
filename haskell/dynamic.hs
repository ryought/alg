import Data.Array
import Data.List
 
buyable n = r!n
    where r = listArray (0,n) (True : map f [1..n])
          f i = i >= 6 && r!(i-6) || i >= 9 && r!(i-9) || i >= 20 && r!(i-20)

-- 合成関数
numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub



