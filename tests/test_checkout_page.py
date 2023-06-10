from src.page_objects.search_page import SearchPage
from src.page_objects.checkout_page import CheckoutPage


def test_checkout(web_drivers):

    product_msg = "iPhone"
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_page.search("Iphone")

    message = search_page.get_message()
    assert product_msg == message, f" message should {product_msg}"

    iphone_checkout = CheckoutPage(*web_drivers)
    iphone_checkout.open()
    iphone_checkout.iphone_checkout("iPhone")