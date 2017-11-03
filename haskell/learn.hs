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

isLarge :: (Ord a, Num a) => a -> String
isLarge x
  | x > 10    = "yep"
  | otherwise = "nppe"


multthree2 :: (Num a) => a -> a -> a
multthree2 x y = x * y

multalt2 :: (Num a) => a -> a
multalt2 x  = let aa = multthree2 10
    in aa x

compareWithHundred :: (Num a, Ord a) => a -> Ordering
compareWithHundred = compare 100
-- compareWithHundred x = compare 100 x

zipWith' :: (a -> b -> c) -> [a] -> [b] -> [c]
zipWith' _ [] _          = []
zipWith' _ _ []          = []
zipWith' f (x:xs) (y:ys) = f x y : zipWith' f xs ys


flip' :: (a -> b -> c) -> (b -> a -> c)
flip' f = g
  where g x y = f y x
-- zipWith' (flip' div) [2, 2 ..] [10, 8, 6, 4, 2]

flipp :: (a -> b -> c) -> (b -> a -> c)
flipp f x y = f y x

flipppp :: (a -> b -> c) -> b -> a -> c  
flipppp f = \x y -> f y x  

-- map map (map (^2)) [[1,2],[3,4,5,6],[7,8]]  
-- map (+3) [1,5,3,1,6] and [x+3 | x <- [1,5,3,1,6]]
-- filter 
filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x:xs)
  | p x = x:filter p xs -- guard  | <condition> = <value>
  | otherwise = filter p xs
  -- let notNull x = not (null x) in filter notNull
  -- [[1,2,3],[],[3,4,5],[2,2],[],[],[]]  
  
largestDivisable :: (Integral a) => a
largestDivisable = head (filter p [1000000, 999999 ..] )
  where p x = x `mod` 3829 == 0

suuum :: (Integral a) => a
suuum = sum (takeWhile (<10000) (filter odd (map (^2) [1 ..])))


chain :: (Integral a) => a -> [a]
chain 1 = [1]
chain n 
  | even n = n:chain (n `div` 2)
  | odd n = n:chain (n*3 + 1)

numLongChains :: Int
numLongChains = length (filter isLong (map chain [1 .. 100]))
  where isLong xs = length xs > 15

numLongChains2 :: Int
numLongChains2 = length (filter (\xs -> length xs > 15) (map chain [1 .. 100]))

hoge :: (Num a, Fractional a) => a -> a -> a
hoge = \a -> \b -> (a*30 + 3)/b

addThree' :: (Num a) => a -> a -> a -> a
addThree' = \x -> \y -> \z -> x + y + z

sum2 :: (Num a) => [a] -> a
sum2 xs = foldl (\acc x -> acc + x) 0 xs
-- left fold

sum3 :: (Num a) => [a] -> a
sum3 = foldl (+) 0

-- foldr/foldl 走査するのに使える
map' :: (a -> b) -> [a] -> [b]
map' f xs = foldr (\x acc -> f x : acc) [] xs
-- map' f xs = foldl (\acc x -> acc ++ [f x]) [] xs

rightassociativefunctionapplication :: Int
rightassociativefunctionapplication = sum $ filter (> 10) $ map (*2) [2 .. 10]

hogehoge :: Bool
hogehoge = and $ map (>4) [5, 6, 7, 8]
