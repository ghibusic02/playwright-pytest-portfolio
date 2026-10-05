import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@pytest.fixture(autouse=True)
def setup(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    
def test_login_valid_user(page: Page):
    
    """" Login with valid user """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.login("standard_user", "secret_sauce")
    
    # Check that the URL was changed and contains inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Check the title of the product page is visible
    expect(inventory_page.page_title).to_have_text("Products")

    
def test_locked_out_user(page: Page):
    """ Login with invalid user """
    login_page = LoginPage(page)    
    login_page.login("locked_out_user", "secret_sauce")
    
    # Check the error container and dispaly the text
    expect(login_page.error_container).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
def test_add_product_to_cart(page:Page):
    """ Login with valid username and password"""
    login_page = LoginPage(page)    
    inventory_page= InventoryPage(page)
    
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack_to_cart()
    
    # check that the cart contains the item that was added and has the value "1"
    expect(inventory_page.cart_badge).to_have_text("1")
    
    
def test_full_checkout_flow(page: Page):
    """ The complete checkout flow until we have the 'Success' message """
    # Login
    login_page = LoginPage(page)    
    inventory_page= InventoryPage(page)
    
    login_page.login("standard_user", "secret_sauce")
    
    # Add a product and go to check the cart
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_checkout_and_fill_form("Corina", "Ghibusi","550304")     
    
    #Check the final message
    expect(inventory_page.success_header).to_have_text("Thank you for your order!")
    
def test_product_sorting_price(page: Page):
    """ Sort the products from Low->High price"""
    # Login
    login_page = LoginPage(page)    
    inventory_page= InventoryPage(page)
    
    login_page.login("standard_user", "secret_sauce")
    inventory_page.sort_by_price_low_to_high()
    
    # Remove the '$' from price and transform them into floats in order to compare them
    prices = inventory_page.get_all_prices()
    
    #Check if the list with the prices is equal with list itself sorted
    assert prices == sorted(prices), f"Prices are not sorted in a correct way: {prices}"
    
    
    
    
    
    
    
    
    
    
    