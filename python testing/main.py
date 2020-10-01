from selenium import webdriver

URL = 'https://teamshift-qa.crossknowledge.com/'
driver = webdriver.Firefox()

def loginTest():
    Enter_on_login_page(URL)
    Insert_email('nefestor@outlook.com')
    Insert_Password('WLS2020qa')


def Enter_on_login_page(url):
    driver.get(URL)
    driver.find_element_by_class_name("button-default").click()


def Insert_email(email):
    driver.implicitly_wait(2)
    driver.find_element_by_id("login-form__login").send_keys(email)
    driver.find_element_by_class_name("js-login-form-submit").click()

def Insert_Password(password):
    driver.implicitly_wait(2)
    driver.find_element_by_id("login-form__password").send_keys(password)
    driver.find_element_by_class_name("js-login-form-submit").click()

loginTest()