from core.router import Router, Route, CallBack

router = Router("File Store Router",
                Route("Main Menu", "Main menu description ...",
                      children=(
                          Route("About us", callback=CallBack("public.utils", "about_us")),
                          Route("User Menu",
                                children=(
                                Route("Insert", callback=CallBack("public.utils", "insert_to_table")),
                                Route("Get", callback=CallBack("public.utils", "about_us")),
                                Route("Undate", callback=CallBack("public.utils", "about_us")),
                                Route("Delete", callback=CallBack("public.utils", "about_us"))
                                )),
                          Route("File Menu", children=(
                              Route("Login", callback=CallBack("public.utils", "salam", name="login")),
                          )),
                      )
                      ))

# Route("About us", callback=CallBack("public.utils", "about_us"))

