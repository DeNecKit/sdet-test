from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

browser: Chrome = None
action_chains: ActionChains = None

def test_init():
    global browser, action_chains
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(options=options)
    browser.get('https://practice-automation.com/form-fields/')
    assert browser != None
    assert browser.title == 'Form Fields | Practice Automation'
    action_chains = ActionChains(browser)

def test_name():
    name_input = browser.find_element(By.XPATH, '//input[@id=\'name-input\']')
    assert name_input != None
    action_chains \
        .move_to_element(name_input) \
        .click() \
        .send_keys('Имя') \
        .perform()

def test_pwd():
    pwd_inputs = browser.find_elements(By.CSS_SELECTOR, 'input[type=password]')
    assert type(pwd_inputs) is list
    assert len(pwd_inputs) == 1
    pwd_input = pwd_inputs[0]
    action_chains \
        .move_to_element(pwd_input) \
        .click() \
        .send_keys('password') \
        .perform()

def test_drinks():
    milk = browser.find_element(By.ID, 'drink2')
    assert milk != None
    action_chains \
        .move_to_element(milk) \
        .click() \
        .perform()
    coffee = browser.find_element(By.ID, 'drink3')
    assert coffee != None
    action_chains \
        .move_to_element(coffee) \
        .click() \
        .perform()

def test_color():
    yellow = browser.find_element(By.ID, 'color3')
    assert yellow != None
    action_chains \
        .move_to_element(yellow) \
        .click() \
        .perform()

def test_like():
    elem = browser.find_element(By.ID, 'automation')
    assert elem != None
    select = Select(elem)
    action_chains.move_to_element(elem).perform()
    select.select_by_visible_text('Yes')

def test_email():
    email = browser.find_element(By.ID, 'email')
    assert email != None
    action_chains \
        .move_to_element(email) \
        .click() \
        .send_keys('name@example.com') \
        .perform()

def get_max_tool(tools):
    return max(tools, key=lambda tool: len(tool.text)).text

def test_msg():
    msg = browser.find_element(By.ID, 'message')
    assert msg != None
    tools = browser.find_elements(By.XPATH,
        '//label[text()=\'Automation tools\']/following::ul/li')
    assert tools != None
    action_chains \
        .move_to_element(msg) \
        .click(msg) \
        .send_keys(f'{len(tools)}\n{get_max_tool(tools)}') \
        .perform()

def test_submit():
    btn = browser.find_element(By.ID, 'submit-btn')
    assert btn != None
    action_chains \
        .move_to_element(btn) \
        .click(btn) \
        .perform()

def test_result():
    sleep(1)
    wait = WebDriverWait(browser, timeout=1)
    alert = wait.until(lambda driver: driver.switch_to.alert)
    assert alert != None
    assert alert.text == 'Message received!'
    alert.accept()
    sleep(1)
    browser.quit()

if __name__ == '__main__':
    test_init()
    test_name()
    test_pwd()
    test_drinks()
    test_color()
    test_like()
    test_email()
    test_msg()
    test_submit()
    test_result()
