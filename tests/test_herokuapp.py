import pytest
from pages.heroku_page import HerokuPage
from playwright.sync_api import Page, expect

def test_1_dynamic_loading(page: Page):
    heroku_page = HerokuPage(page)
    heroku_page.navigate_to_dynamic_loading()
    
    # Click on Start and a loading animation will be dispalyed
    heroku_page.trigger_dynamic_loading()
    
    # Check if the element is visible
    expect(heroku_page.finish_text).to_be_visible(timeout=10000)
    #expect(heroku_page.finish_text).to_have_text("Hello World!", timeout=10000)
    
def test_2_javascript_alert(page: Page):
    heroku_page = HerokuPage(page)
    
    heroku_page.navigate_to_javascript_alerts()
    # When the pop-up will be dispalyed ,the dialog will be catched and run accept() method
    page.on("dialog", lambda dialog: dialog.accept())
    # Press the button for the pop-up
    heroku_page.js_alert_button.click()
    # we check that the alert was successfully accepted  
    expect(heroku_page.result_text).to_have_text("You successfully clicked an alert")