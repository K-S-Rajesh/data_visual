from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Configuration ---
# Update these with your webpage's login details and element locators
LOGIN_URL = "https://portal.kct.ac.in/index.php/Login"  # Replace with the actual URL
USERNAME = "vishnuprakash.b@kctbs.ac.in"  # Replace with your username
PASSWORD = "93D5lmOP"  # Replace with your password
# Locators (update these based on your webpage's HTML inspection)
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "password1"
CAPTCHA_FIELD_ID = "captcha"
SUBMIT_BUTTON_XPATH = "//*[@id='login']"


# ---------------------

def automate_login_with_manual_captcha():
    # Initialize the browser
    driver = webdriver.Chrome()  # Make sure the driver is in your system's PATH or provide the path
    driver.get(LOGIN_URL)
    driver.maximize_window()  # Optional: maximize window for better visibility

    try:
        # 1. Fill in username and password fields
        # Wait a moment for the page to load
        time.sleep(2)

        username_field = driver.find_element(By.ID, USERNAME_FIELD_ID)
        username_field.send_keys(USERNAME)

        password_field = driver.find_element(By.ID, PASSWORD_FIELD_ID)
        password_field.send_keys(PASSWORD)

        print("Username and password entered.")

        # 2. PAUSE for manual CAPTCHA entry
        # The script stops here and waits for your input in the console
        captcha_value = input("Please look at the browser, solve the CAPTCHA, and enter the code here: ")

        # 3. Enter the manually provided CAPTCHA value
        captcha_field = driver.find_element(By.ID, CAPTCHA_FIELD_ID)
        captcha_field.send_keys(captcha_value)

        print(f"CAPTCHA '{captcha_value}' entered. Submitting the form...")

        # 4. Submit the form
        submit_button = driver.find_element(By.XPATH, SUBMIT_BUTTON_XPATH)
        submit_button.click()

        # Wait briefly to see the result of the login attempt
        time.sleep(5)
        print("Login process finished.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Keep the browser open so you can see the final state, you can change this
        # driver.quit()
        pass

# Run the function
automate_login_with_manual_captcha()
