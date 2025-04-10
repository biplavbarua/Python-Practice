from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import ssl

# Ensure SSL is enabled
try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass

# Configuration
USERNAME = "biplavbarua"
PASSWORD = "Movies@9737"
TARGET_USER = "vilibazmio"
FOLLOW_LIMIT = 10  # Set the max number of users to follow per run

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

def login():
    driver.get("https://letterboxd.com/sign-in/")
    time.sleep(3)  # Wait for the page to load
    try:
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]")
        
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        login_button.click()
        
        time.sleep(5)  # Allow time for login to complete
        
        # Verify login success
        if "Sign in" in driver.page_source:
            print("Login failed! Incorrect credentials or blocked.")
            return False
        
        print("Logged in successfully!")
        return True
    except Exception as e:
        print("Login failed:", e)
        return False

def follow_users():
    driver.get(f"https://letterboxd.com/{TARGET_USER}/followers/")
    time.sleep(5)  # Wait for followers page to load
    
    followed_count = 0
    while followed_count < FOLLOW_LIMIT:
        follow_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Follow')]")
        
        if not follow_buttons:
            print("No more users to follow or unable to find follow buttons.")
            break
        
        for button in follow_buttons:
            if followed_count >= FOLLOW_LIMIT:
                break
            try:
                driver.execute_script("arguments[0].scrollIntoView();", button)  # Ensure button is visible
                time.sleep(1)  # Add slight delay before clicking
                button.click()
                followed_count += 1
                print(f"Followed {followed_count} users.")
                time.sleep(3)  # Add delay to mimic human behavior
            except Exception as e:
                print("Error clicking follow button:", e)
                continue
        
        # Scroll down to load more users
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Allow new users to load
    
    print("Follow process completed!")

def main():
    if login():
        follow_users()
    driver.quit()

if __name__ == "__main__":
    main()
