from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator   = page.locator("[data-test='login-button']")
        self.error_container: Locator= page.locator("[data-test='error']")
        
        
    def navigate(self):
        """ Open login page """
        self.page.goto("https://saucedemo.com")
        
    def login(self, username: str, password: str):
        """ This method will be reused for login """
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        
    def get_error_message(self) ->str:
        """ Will return the error message in case the login failed """
        return self.error_container.text_content()
    
    