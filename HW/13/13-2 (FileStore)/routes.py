from core.router import Router, Route, CallBack

router = Router("File Store Router",
                Route("Main Menu", "Main menu description ...",
                      children=(
                          Route("About us", callback=CallBack("public.utils", "about_us")),
                          Route("User Menu", children=(
                                Route("Insert", callback=CallBack("public.utils", "insert_to_table", model_class = "User")),
                                Route("Get", callback=CallBack("public.utils", "read_from_table", model_class = "User")),
                                Route("Update", callback=CallBack("public.utils", "update_in_table", model_class = "User")),
                                Route("Delete", callback=CallBack("public.utils", "delete_from_table", model_class = "User"))
                                )),
                          Route("File Menu", children=(
                                Route("Insert", callback=CallBack("public.utils", "insert_to_table", model_class = "File")),
                                Route("Get", callback=CallBack("public.utils", "read_from_table", model_class = "File")),
                                Route("Update", callback=CallBack("public.utils", "update_in_table", model_class = "File")),
                                Route("Delete", callback=CallBack("public.utils", "delete_from_table", model_class = "File"))
                          )),
                      )
                      ))

# Route("About us", callback=CallBack("public.utils", "about_us"))

