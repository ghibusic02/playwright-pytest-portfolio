from playwright.sync_api import Page, Locator
import os

class InteractionsPage:
    def __init__(self, page: Page):
        self.page = page
        # Locators for File Upload
        self.file_input: Locator = page.locator("#file-upload")
        self.upload_submit_button: Locator = page.locator("#file-submit")
        self.uploaded_file_text : Locator = page.locator("#uploaded-files")
        
        # Locatior for Drag and Drop
        self.drag_source: Locator = page.locator("#column-a")
        self.drop_target: Locator = page.locator("#column-b")
        self.drop_button: Locator = page.locator("#simulate-drag")
        
        # Locators for Radio Buttons
        self.radio_card: Locator = page.locator("#radio-card")
        self.radio_cash: Locator = page.locator("#radio-cash")
        
        # Locators for Hover Menu
        self.hover_button: Locator = page.locator("#hover-menu-button")
        self.hover_link_1: Locator = page.locator("#link-option-1")
        
        # Web Table
        # Select the first row with data regarding the employee
        self.table_row_corina: Locator = page.locator("#table-employee tr").nth(1)


        
    def navigate_to_local_page(self):
        html_path = os.path.abspath("localPageToTest.html") 
        self.page.goto(f"file://{html_path}")
        