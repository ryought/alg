maximum' :: (Ord a) => [a] -> a
maximum' [] = error "empty list"
maximum' [x] = x
maximum' (x:xs)
  | x > maxTail = x
  | otherwise = maxTail
  where maxTail = maximum' xs

-- Num: addition, Ord: comparison
replicate' :: (Num i, Ord i) => i -> a -> [a]
replicate' n x
  | n <= 0 = []
  | otherwise = x:replicate' (n-1) x

take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
  | n <= 0 = []
take' _ [] = []
take' n (x:xs) = x:take' (n-1) xs

factorial :: Integer -> Integer
factorial n = product [1..n]

fib :: (Integral a) => a -> a
fib 1 = 1
fib 2 = 1
fib x = fib (x-1) + fib (x-2)

removeNonUpperCase :: [Char] -> [Char]
removeNonUpperCase st = [ c | c <- st, c `elem` ['A'..'Z']]
-- [Type]
-- Int: integer,  Integer: unbounded integer, Float, Double
addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

-- [TypeClass] TypeのClass  typeの属する集合
-- Eq(can use ==), Ord( <= ), Show, Read, Enum, Bounded, 
-- Num, Integral(Int Integer), Floating(=Float, Double)
luckey :: (Integral a) => a -> String
luckey 7 = "Heyy"
luckey x = "out of luck"

first :: (a, b, c) -> a
first (x, _, _) = x

head' :: [a] -> a
head' [] = error "emtpy"
head' (x:_) = x

head'' :: [a] -> a  
head'' xs = case xs of [] -> error "No head for empty lists!"  
                       (x:_) -> x

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

max' :: (Ord a) => a -> a -> a
max' a b
  | a > b    = a
  | otherwise = b
-- スペースは大事
initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ ". "
    where (f:_) = firstname
          (l:_) = lastname

calcBmis :: (RealFloat a) => [(a,a)] -> [a]
calcBmis xs = [bmi w h | (w, h) <- xs]
    where bmi weight height = weight / height ^ param
          param = 2

-- where binding:  can refer from anywhere in function
-- let in binging: can refer only from "in" expression
cylinder :: (RealFloat a) => a -> a -> a
cylinder r h = 
    let sideArea = 2 * pi * r * h
        topArea = pi * r^2
    in sideArea + 2 * topArea

zip' :: [a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x,y):zip' xs ys

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) =
  let smallerSorted = quicksort [ a | a <- xs, a <= x ]
      biggerSorted  = quicksort [ a | a <- xs, a >  x ]
  in smallerSorted ++ [x] ++ biggerSorted

maxho :: (Ord a, Num a) => a -> a
maxho x = max 4 x

devideByTen :: (Floating a) => a -> a
devideByTen = (/10)
-- because
-- *Main> :t (/10)
-- (/10) :: Fractional a => a -> a
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)
