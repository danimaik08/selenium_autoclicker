import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://mozgion.ru/test-trenazher-na-skorost-reakcii/')

counter = 0
MAX_COUNTER = 5

button = browser.find_element(By.ID, 'stage')
browser.execute_script('window.scrollTo(0, 300);')

while counter < MAX_COUNTER:
    button.click()

    while True:
        if button.get_dom_attribute('class') == 'stage training go':
            counter += 1
            browser.execute_script("document.getElementById('stage').dispatchEvent(new Event('mousedown'));")
            break

    button.click()

time.sleep(5)