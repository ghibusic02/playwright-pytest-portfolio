from playwright.sync_api import Page,Locator

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        
        #Locators
        self.page_title: Locator = page.locator("[data-test='title']")
        self.backpack_add_to_cart: Locator = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")
        self.cart_link: Locator = page.locator("[data-test='shopping-cart-link']")
        self.checkout_button: Locator = page.locator("[data-test='checkout']")
    
        # Checkout form
        self.firstName: Locator = page.locator("[data-test='firstName']")
        self.LastName: Locator = page.locator("[data-test='lastName']")
        self.postal_code: Locator = page.locator("[data-test='postalCode']")
        self.continue_button: Locator = page.locator("[data-test='continue']")
        self.finish_button: Locator = page.locator("[data-test='finish']")
        self.success_header: Locator = page.locator("[data-test='complete-header']")
        
        # Sorting the products
        self.sort_container: Locator = page.locator("[data-test='product-sort-container']")
        self.item_prices: Locator = page.locator("[data-test='inventory-item-price']")
        
    def add_backpack_to_cart(self):
        self.backpack_add_to_cart.click()
        
    def go_to_checkout_and_fill_form(self, first: str, last: str, zipCode: str):
        self.cart_link.click()
        self.checkout_button.click()
        self.firstName.fill(first)
        self.LastName.fill(last)
        self.postal_code.fill(zipCode)
        self.continue_button.click()
        self.finish_button.click()
        
    def sort_by_price_low_to_high(self):
        self.sort_container.select_option("lohi")
        
    def get_all_prices(self)->list[float]:
        price_strings = self.item_prices.all_text_contents()
        return [float(p.replace("$","")) for p in price_strings]
    
        

        