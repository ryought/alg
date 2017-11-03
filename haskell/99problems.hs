-- p1
myLast :: [a] -> a
myLast x = head $ reverse x
-- myLast = last

myLast2 :: [a] -> a
myLast2 [] = error "hoge"
myLast2 [x] = x
myLast2 (_:xs) = myLast xs

-- p2
myButLast :: [a] -> a
myButLast x = head $ tail $ reverse x
-- head . tail . reverse
-- reverse x !! 1

myButLast2 :: [a] -> a
myButLast2 [] = error "hoge"
myButLast2 [x] = error "only one elem"
myButLast2 (x:_:[]) = x
myButLast2 (x:xs) = myButLast2 xs
-- (x:xs) = if length xs == 1 then x else mybut xs

myButLast' [x,_] = x  -- ２文字からなるリスト [x,_] でもあり (x:_:[]) (x:(_:[])) でもある
myButLast' (_:xs) = myButLast' xs

-- p3
elementAt :: [a] -> Int -> a
elementAt list i = list !! (i-1)

elementAt' :: [a] -> Int -> a
elementAt' x 1 = head x -- head,tailが取れない場合は？
elementAt' x i = elementAt' (tail x) (i - 1)
-- head/tail  init/last
-- これだと取れない場合がある 例外処理すると次のやつになる
elementAt'' :: [a] -> Int -> a
elementAt'' (x:_) 1  = x
elementAt'' (_:xs) i = elementAt'' xs (i-1)
elementAt'' _ _ = error "index out of bounds"

-- p4
myLength :: [a] -> Int
myLength [] = 0
myLength [x] = 1
myLength (x:xs) = 1 + (myLength xs)

myLength2 :: [a] -> Int
myLength2 x = innerLength x 0
  where innerLength [] y = y
        innerLength (_:xs) y = innerLength xs (y+1) -- tailとかは使わず、パターンマッチさせる

myLength3 :: [a] -> Int
myLength3 = foldl (\acc _ -> acc + 1) 0

myLength4 :: [a] -> Int
myLength4 = sum . map (\_ -> 1)

-- p5
-- myReverse :: [a] -> [a]
myReverse :: [a] -> [a]
myReverse [x] = [x] 
myReverse (x:xs) = (myReverse xs) ++ [x]

--p6
isPalindrome :: (Eq a) => [a] -> Bool
isPalindrome [x] = True
isPalindrome (left:center:right) = if left == right
                                     then isPalindrome center
                                     else False

