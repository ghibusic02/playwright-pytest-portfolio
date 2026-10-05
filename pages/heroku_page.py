from playwright.sync_api import Page, Locator

class HerokuPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators for Dynamic Loading
        self.start_button: Locator = page.locator("div#start > button")
        self.finish_text: Locator = page.locator("text=Hello World!")
        
        # Locators for JavaScript Alerts
        self.js_alert_button: Locator = page.locator("button[onclick='jsAlert()']")
        self.result_text: Locator = page.locator("p#result")
        
    def navigate_to_dynamic_loading(self):
        """ Open the page with the hidden dynamic element """
        self.page.goto("https://the-internet.herokuapp.com/dynamic_loading/1", timeout=60000)

    def navigate_to_javascript_alerts(self):
        """ Open the page with javascript alerts pop-up """
        self.page.goto("https://the-internet.herokuapp.com/javascript_alerts", timeout=60000)
        
    def trigger_dynamic_loading(self):
        self.start_button.click()
    
            
        