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
    