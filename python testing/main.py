from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://teamshift-qa.crossknowledge.com/'
driver = webdriver.Firefox()

def loginTest():
    Enter_on_login_page(URL)
    Insert_email('nefestor@outlook.com')
    Insert_Password('WLS2020qa')
    driver.close()

def Enter_on_login_page(url):
    driver.get(URL)
    driver.find_element_by_class_name("button-default").click()


def Insert_email(email):
    driver.find_element_by_id("login-form__login").send_keys(email)
    driver.find_element_by_class_name("js-login-form-submit").click()

def Insert_Password(password):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, "login-form__password")))
    element.send_keys(password)
    driver.find_element_by_class_name("js-login-form-submit").click()

loginTest()