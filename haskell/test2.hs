main = do putStrLn "What is 2+2?"
          x <- readLn
          if x == 4
            then putStrLn "youare right"
            else putStrLn "not"


