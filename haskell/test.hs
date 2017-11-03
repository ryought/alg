instance RenderRoute HelloWorld where
    data Route HelloWorld = HomeR
        deriving (Show, Eq, Read)
    renderRoute HomeR = ([], [])

instance ParseRoute HelloWorld where
    parseRoute ([], _) = Just HomeR
    parseRoute _       = Nothing

instance YesodDispatch HelloWorld where
    yesodDispatch env req =
        yesodRunner handler env mroute req
      where
        mroute = parseRoute (pathInfo req, textQueryString req)
        handler =
            case mroute of
                Nothing -> notFound
                Just HomeR ->
                    case requestMethod req of
                        "GET" -> getHomeR
                        _     -> badMethod

type Handler = HandlerT HelloWorld IO
