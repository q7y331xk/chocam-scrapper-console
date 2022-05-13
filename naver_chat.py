from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from auth.auth import naver_login
from config import SILENCE

def get_chat():
    login = naver_login(SILENCE)
    driver = login['driver']
    driver.get(f"https://talk.cafe.naver.com/channels")
    return driver
    
def remove_chat_by_idx(driver, reads, idx):
    reads[idx].find_element(By.CLASS_NAME,'link_more').click()
    sleep(1)
    reads[idx].find_elements(By.CLASS_NAME,'link')[1].click()
    sleep(1)
    alert = Alert(driver)
    alert.accept()
    sleep(1)
        
def remove_chats(chats_cnt):
    
    driver = get_chat()
    sleep(1)
    reads = driver.find_elements(By.CLASS_NAME,'read')
    reads_len = len(reads)
    i = 1
    while (i <= chats_cnt):
        idx = reads_len - i
        remove_chat_by_idx(driver, reads, idx)
        i = i + 1