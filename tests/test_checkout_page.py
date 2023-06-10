from src.page_objects.register_page import RegisterPage
from src.page_objects.search_page import SearchPage
from src.page_objects.product_page import ProductPage
from src.page_objects.account_page import AccountPage
from src.page_objects.login_page import LoginPage

def test_checkout(web_drivers):

    product_msg = "iPhone"
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_page.search("Iphone")

    message = search_page.get_message()
    assert product_msg == message, f" message should {product_msg}"

    iphone_page = ProductPage(*web_drivers)
    iphone_page.open()
    iphone_page.iphone_search("iPhone")