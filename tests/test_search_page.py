from src.page_objects.search_page import SearchPage


def test_register(web_drivers):
    product_msg = "iPhone"
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_page.search("Iphone")

    message = search_page.get_message()
    assert product_msg == message, f" message should {product_msg}"
