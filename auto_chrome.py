from selenium import webdriver
import pyautogui as pa
import time
from selenium.webdriver.common.keys import Keys

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)
    elem = browser.get('https://www.agame.com/game/magic-piano-tiles')
    time.sleep(5)
    pa.press('f11')
    elem = browser.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(2)
    elem = browser.find_element_by_class_name('icon--fullscreen').click()

