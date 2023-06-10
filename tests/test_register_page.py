from src.page_objects.register_page import RegisterPage



def test_register(web_drivers):
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.register("Aaron", "Bernal", "jessarn010@gmail.com", "5623613748", "qaminds12345", "qaminds12345")




