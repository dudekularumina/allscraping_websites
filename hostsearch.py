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
# chrome_options.add_argument("--incognito")  # Open in incognito mode
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

try:
    # Open the website
    driver.get("https://forums.hostsearch.com/")
    
    # Click on the Register button
    register_button = driver.find_element(By.XPATH, "//a[text()='Register']")
    register_button.click()
    
    # Wait for the registration page to load
    WebDriverWait(driver, 10).until(EC.url_contains("hsforums_registration.php"))
    
    # Print the current URL
    print("Current URL:------------", driver.current_url)
    
    # Input username
    username_input = driver.find_element(By.ID, "regusername")
    username_input.send_keys("dudekularumina")
    time.sleep(3)
    
    # Input password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Rumina@41228")
    time.sleep(3)
    
    # Input confirm password
    password_confirm_input = driver.find_element(By.ID, "passwordconfirm")
    password_confirm_input.send_keys("Rumina@41228")
    time.sleep(3)
    
    # Input email
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys("ruminadudekula41228@gmail.com")
    time.sleep(3)
    
    # Confirm email (Assuming it's the same as the email field)
    confirm_email_input = driver.find_element(By.ID, "emailconfirm")
    confirm_email_input.send_keys("ruminadudekula41228@gmail.com")
    time.sleep(3)
    
    # Handle reCAPTCHA
    try:
        wait = WebDriverWait(driver, 10)

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

    
    # Agree to term
    time.sleep(10)
    agree_checkbox = driver.find_element(By.XPATH, '//*[@id="cb_rules_agree"]') # Corrected the quotes
    time.sleep(2)
    agree_checkbox.click()
    time.sleep(3)
    
    # Click on the Complete Registration button
    complete_registration_button = driver.find_element(By.XPATH, "//input[@value='Complete Registration']")
    complete_registration_button.click()
    
    # Wait for a few seconds to ensure the action is completed
    time.sleep(10)
    print("Current URL after registration:----------------", driver.current_url)
    
    # Navigate to profile page
    driver.get("https://forums.hostsearch.com/profile.php?do=editprofile")
    time.sleep(5)
    
    print("Current URL after profile:----------------", driver.current_url)
    
    # Update homepage URL
    time.sleep(5)
    homepage_input = driver.find_element(By.ID, "tb_homepage")
    homepage_input.send_keys("https://mysamplesite.com") #sampleurl
    time.sleep(3)
    
    # Click on "Edit Signature"
    edit_signature_link = driver.find_element(By.XPATH, "//a[text()='Edit Signature']")
    edit_signature_link.click()
    
    # Wait for the signature editing page to load
    WebDriverWait(driver, 20).until(EC.url_contains("profile.php?do=editsignature"))
    print("Current URL after clicking 'Edit Signature':----------------", driver.current_url)
    time.sleep(5)
    driver.get(driver.current_url)
    
    # Add sample URLs to the signature
    signature_textarea = driver.find_element(By.CSS_SELECTOR, "textarea.cke_source")
    time.sleep(5)

    signature_textarea.clear()
    time.sleep(5)
    #Adding sample urls
    signature_textarea.send_keys("[URL=\"http://mysite1.com\"]http://mysite1.com[/URL]\n[URL=\"http://mysite2.com\"]http://mysite2.com[/URL]")
    
    # Click on "Save Signature"
    time.sleep(3)
    save_signature_button = driver.find_element(By.CSS_SELECTOR, "input[value='Save Signature']")
    time.sleep(3)

    save_signature_button.click()
    time.sleep(3)
    
    # Click on the Profile element with the specified XPath
    top_link = driver.find_element(By.XPATH, "//*[@id='toplinks']/ul/li[3]/a")
    top_link.click()
    time.sleep(5)
    
    # Print the current URL
    print("Current URL after clicking top link:----------------", driver.current_url)
    driver.get(driver.current_url)
    time.sleep(3)
    
    # Click on the "About Me" tab
    about_me_tab = driver.find_element(By.ID, "aboutme-tab")
    about_me_tab.click()
    time.sleep(5)
    
    # Print the current URL
    print("Current URL after clicking 'About Me':----------------", driver.current_url)
    time.sleep(15)


finally:
    # Close the browser
    driver.quit()

