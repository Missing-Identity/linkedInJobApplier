import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps Chrome Open even after the script is done
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

linkedin_link = input("Enter the LinkedIn Job Search URL: ")
driver.get(linkedin_link)

load_dotenv()

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys(os.getenv("USERNAME"))
password.send_keys(os.getenv("PASSWORD"))
submit = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container button")
submit.click()
time.sleep(5)

jobs = driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container .jobs-search-results__list-item")
for job in jobs:
    try:
        job.click()
        time.sleep(2)
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        easy_apply.click()
        time.sleep(2)
        next_btn = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        next_btn.click()
        resume_choose = driver.find_element(By.CSS_SELECTOR,
                                            ".jobs-resume-picker__resume .jobs-resume-picker__resume-btn-container "
                                            "button")
        resume_choose.click()
        time.sleep(2)
        resume_next = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        resume_next.click()
        time.sleep(2)
        review = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        review.click()
        time.sleep(2)
        if driver.find_element(By.CSS_SELECTOR, ".artdeco-inline-feedback__message"):
            print("Application cannot be submitted")
            dismiss = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            dismiss.click()
            time.sleep(2)
            discard = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
            discard.click()
            continue
        else:
            submit = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
            submit.click()
            time.sleep(2)
            print("Application submitted")
            dismiss = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            dismiss.click()
    except NoSuchElementException:
        print("No Easy Apply")
        dismiss = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
        dismiss.click()
