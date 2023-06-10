from src.page_objects.search_page import SearchPage
from src.page_objects.product_page import ProductPage


def test_select_iphone(web_drivers):
    iphone_page = ProductPage(*web_drivers)
    iphone_page.open()
    iphone_page.iphone_search("iPhone")
