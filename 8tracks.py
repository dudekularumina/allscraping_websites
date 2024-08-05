from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# Anti-Captcha API key
API_KEY = '8a49a20ff3faacb672dcee697adec6f0'

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Open in incognito mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent detection

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

def solve_recaptcha(site_key, url):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key(API_KEY)
    solver.set_website_url(url)
    solver.set_website_key(site_key)

    response = solver.solve_and_return_solution()
    if response != 0:
        return response
    else:
        print("Task finished with error: " + solver.error_code)
        return None

# Open the website
driver.get("https://8tracks.com/")

try:
    # Wait for the link to load and then click it
    wait = WebDriverWait(driver, 20)
    try:
        link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.flatbutton.button_gradient")))
        link.click()
        print("Link clicked")
    except Exception as e:
        print(f"Link clicking failed: {e}")

    # Print the current URL
    print("Current URL:", driver.current_url)

    # Fill out the email field
    email_input = wait.until(EC.presence_of_element_located((By.ID, "user_email")))
    email_input.send_keys("ruminadudekula41228@gmail.com")
    time.sleep(2)

    # Fill out the username field
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user_login")))
    username_input.send_keys("ruminadudekula")
    time.sleep(2)

    # Fill out the password field
    password_input = wait.until(EC.presence_of_element_located((By.ID, "user_password")))
    password_input.send_keys("Rumina@41228")
    time.sleep(2)

    # Handle reCAPTCHA
    try:
        iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='recaptcha']")))
        driver.switch_to.frame(iframe)
        print("Switched to reCAPTCHA iframe")
        time.sleep(2)

        recaptcha_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "recaptcha-anchor")))
        recaptcha_checkbox.click()
        print("reCAPTCHA checkbox clicked")
        time.sleep(2)

        driver.switch_to.default_content()
        print("Switched back to default content")

        # Solve reCAPTCHA
        site_key = driver.find_element(By.CLASS_NAME, 'g-recaptcha').get_attribute('data-sitekey')
        current_url = driver.current_url
        recaptcha_response = solve_recaptcha(site_key, current_url)

        if recaptcha_response:
            driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{recaptcha_response}";')
            print("reCAPTCHA solved")
            time.sleep(2)
        else:
            print("Failed to solve reCAPTCHA")
            

    except Exception as e:
        print(f"CAPTCHA handling failed: {e}")

    # Click the "Sign up" button using JavaScript
    signup_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submit")))
    driver.execute_script("arguments[0].click();", signup_button)
    print("Sign up button clicked")

    # Wait to see the result of the click
    time.sleep(10)
    print("Current URL:", driver.current_url)
    driver.back()
    driver.get("https://8tracks.com/ruminadudekula")

finally:
    driver.quit()
