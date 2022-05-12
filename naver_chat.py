from bs4 import BeautifulSoup
from auth.auth import naver_login
from config import SILENCE

login = naver_login(SILENCE)
driver = login['driver']
driver.get(f"https://talk.cafe.naver.com/channels")
chat_soup = BeautifulSoup(driver.page_source, 'html.parser')
print(chat_soup)