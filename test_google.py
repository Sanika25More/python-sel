from selenium import webdriver
import pytest

def test_google_search():
    # Open Chrome browser
    driver = webdriver.Chrome()

    # Go to Google
    driver.get("https://www.google.com")

    # Verify title contains "Google"
    assert "Google" in driver.title

    # Close browser
    driver.quit()

