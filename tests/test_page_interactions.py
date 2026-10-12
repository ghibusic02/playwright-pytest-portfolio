import os
import pytest
from playwright.sync_api import Page, expect
from pages.interactions_page import InteractionsPage


def test_1_file_upload(page: Page):
    """ Upload a file from computer """
    interactions_page = InteractionsPage(page)
    interactions_page.navigate_to_local_page()
    
    # Create a temporar file on the computer 
    file_name = "test_fileName.txt"
    with open(file_name, "w") as f:
        f.write("Automated test successfully executed in Playwrite")
    
    # Get the absolute path for the file   
    file_path = os.path.abspath(file_name)
    # Upload the file on the site
    interactions_page.file_input.set_input_files(file_path)
    # Press submit button
    interactions_page.upload_submit_button.click()
    # Check to see if the name of the file was loaded
    expect(interactions_page.uploaded_file_text).to_have_text(file_name, timeout=2000)
    
    # Remove the temporar file on the computer
    if os.path.exists(file_name):
        os.remove(file_name)
        
def test_2_drag_and_drop(page: Page):
    interaction_page = InteractionsPage(page)
    interaction_page.navigate_to_local_page()
    
    interaction_page.drop_button.click()    
    
    # Check if the text was changed
    expect(interaction_page.drag_source).to_have_text("B",timeout=2000)
    
def test_3_radio_buttons(page: Page):
    """ Check the unique selection from a list with radio buttons """
    interaction_page = InteractionsPage(page)
    interaction_page.navigate_to_local_page()
    
    # Check to see if the options are not selected
    expect(interaction_page.radio_card).not_to_be_checked()
    expect(interaction_page.radio_cash).not_to_be_checked()
    
    # check the payment with the credit card
    interaction_page.radio_card.check()
    expect(interaction_page.radio_card).to_be_checked()
    expect(interaction_page.radio_cash).not_to_be_checked()
    
    
def test_4_hover_menu(page: Page):
    """ Simulate mouse hover to display a hidden element """
    
    interaction_page = InteractionsPage(page)
    interaction_page.navigate_to_local_page()
    
    # Normally the hidden link should not be visible
    expect(interaction_page.hover_link_1).not_to_be_visible()
    
    # Use the .hover function to move the mouse over the button
    interaction_page.hover_button.hover()
    
    # Check to see if the link is now visible
    expect(interaction_page.hover_link_1).to_be_visible()
    
    
def test_5_table_validation(page: Page):
    """ Validate data from a dinamic table( Web Table) """
    interaction_page = InteractionsPage(page)
    interaction_page.navigate_to_local_page()
    
    expect(interaction_page.table_row_corina).to_contain_text("QA Automation") 
    expect(interaction_page.table_row_corina).to_contain_text("Sibiu")       
    