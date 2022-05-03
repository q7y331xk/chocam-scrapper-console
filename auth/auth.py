import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from config import NAVER_ID, NAVER_PW

def set_cookies(cookies):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    session = requests.Session()
    session.headers.update(headers)
    for cookie in cookies:
        c = {cookie['name']: cookie['value']}
        session.cookies.update(c)
    return session

def set_chrome_driver(silence):
    chrome_options = webdriver.ChromeOptions()
    if silence:
        chrome_options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def naver_login(silence):
    driver = set_chrome_driver(silence)
    driver.get("https://nid.naver.com/nidlogin.login")
    pyperclip.copy(NAVER_ID)
    driver.find_element(By.ID,'id').click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    sleep(1)
    pyperclip.copy(NAVER_PW)
    driver.find_element(By.ID,'pw').click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
    sleep(1)
    driver.find_element(By.ID,'log.login').click()
    cookies = driver.get_cookies()
    return { 'driver': driver, 'cookies': cookies}
