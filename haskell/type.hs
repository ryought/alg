data Point = Point Float Float deriving (Show)
data Shape = Circle Point Float | Rectangle Point Point deriving (Show)


surface :: Shape -> Float
surface (Circle _ r) = pi * r ^ 2
surface (Rectangle (Point x1 y1) (Point x2 y2)) = (abs $ x2 - x1) * (abs $ y2 - y1)


data Person = Person String String Int Float deriving (Show)

firstName'  :: Person -> String
firstName' (Person firstname  _ _ _) = firstname

data Person2 = Person2 { firstName :: String
             , lastName :: String
             , age :: Int
             , height :: Float
             , phoneNumber :: String
             , flavor :: String
} deriving (Show)
