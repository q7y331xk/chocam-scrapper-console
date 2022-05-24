from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import UnexpectedAlertPresentException
from scrapping.naver_chat import remove_chats

def get_article_ids(driver):
    article_ids = []
    driver.get(f"https://cafe.naver.com/chocammall?iframe_url=/ArticleList.nhn%3Fsearch.clubid=20486145%26search.menuid=214%26search.boardtype=L")
    i = 0
    while(True):
        sleep(1)
        i = i + 1
        driver.switch_to.frame('cafe_main')
        board_soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = board_soup.find_all('div', {'class': 'article-board m-tcol-c'})
        if table:
            break
        if i > 50:
            driver.get(f"https://cafe.naver.com/chocammall?iframe_url=/ArticleList.nhn%3Fsearch.clubid=20486145%26search.menuid=214%26search.boardtype=L")
            sleep(1)
    trs = table[1].find_all("tr")
    for tr in trs:
        article_number = tr.find('div',{'class':'inner_number'})
        if article_number:
            article_ids.append(int(article_number.text))
    return article_ids

def get_pdp_soup(driver, article_id):
    driver.get(f"https://cafe.naver.com/chocammall?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D20486145%2526page%3D1%2526menuid%3D214%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dfalse")
    sleep(1)
    driver.switch_to.frame('cafe_main')
    while True:
        i = 0
        pdp_soup = BeautifulSoup(driver.page_source, 'html.parser')
        section = pdp_soup.find('div', {'class': 'section'})
        if section:
            break
        else:
            se_section = pdp_soup.find('div', {'class': 'se-section'})
            if se_section:
                pdp_soup = 'pass'
                break
            error = pdp_soup.find('div', {'class': 'error_content'})
            if error:
                driver.get(f"https://cafe.naver.com/chocammall?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D20486145%2526page%3D1%2526menuid%3D214%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dfalse")
                sleep(1)
                driver.switch_to.frame('cafe_main')
                     
        sleep(1)
        i = i + 1
        if i > 50:
            driver.get(f"https://cafe.naver.com/chocammall?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D20486145%2526page%3D1%2526menuid%3D214%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dfalse")
            sleep(1)
            driver.switch_to.frame('cafe_main')
    
    return { "article_id": article_id, "pdp_soup": pdp_soup }

def convert_soup_to_dict(pdp_soup_obj):
    pdp_dict = {}
    pdp_soup = pdp_soup_obj["pdp_soup"]
    pdp_dict['article_id'] = pdp_soup_obj["article_id"]
    pdp_soup.find('div', {'class': 'section'}).find('div',{'class': 'LayerArticle'}).decompose()
    title = pdp_soup.find('h3')
    if title:
        pdp_dict['title'] = title.text.strip().replace('"', ' ')
    cost = pdp_soup.find('strong', {'class':'cost'})
    if cost:
        pdp_dict['cost'] = int(cost.text.strip().replace(',','').replace('원',''))
    detail_list = pdp_soup.find('div', {'class': 'section'}).find_all('dl', {'class':'detail_list'})
    details = []
    for detail_item in detail_list:
        detail_title = detail_item.find('dt')
        if detail_title:
            detail_title = detail_title.text.strip()
        detail_content = detail_item.find('dd')
        if detail_content:
            detail_content = detail_content.text.strip().replace('  ', '').replace('\n', '')
        details.append({f'{detail_title}': f'{detail_content}'})
    pdp_dict['details'] = details
    phone = pdp_soup.find('p', {'class':'tell'})
    if phone:
        pdp_dict['phone'] = phone.text.strip()
    else:
        pdp_dict['phone'] = 'chat'

    nickname = pdp_soup.find('div', {'class':'nick_box'})
    if nickname:
        pdp_dict['nickname'] = nickname.text.strip()
    status = pdp_soup.find('p', {'class': 'ProductName'}).find('em')
    if status:
        pdp_dict['status'] = status.text.strip()
    date = pdp_soup.find('span', {'class':'date'})
    if date:
        pdp_dict['date'] = date.text.strip()
    views = pdp_soup.find('span', {'class':'count'})
    if views:
        pdp_dict['views'] = int(views.text.replace('조회', '').strip())
    main = pdp_soup.find('div', {'class':'se-main-container'})
    if main:
        pdp_dict['main'] = main.text.strip().replace('\n', '').replace('\u200b', '').replace('"', ' ')
    else:
        pdp_dict['main'] = "body 크롤링 실패"
    pdp_dict['comments_cnt'] = int(pdp_soup.find('strong', {'class':'num'}).text.strip())
    comments = pdp_soup.find('ul', {'class':'comment_list'})
    if comments:
        pdp_dict['comments'] = comments.text.strip().replace('  ', '').replace('\n', '').replace('답글쓰기', '').replace('"', ' ')
    else:
        pdp_dict['comments'] = ''
    likes = pdp_soup.find('div',{'class':'like_article'}).find('em', {'class': "u_cnt _count"})
    if likes:
        pdp_dict['likes'] = int(likes.text)
    return pdp_dict

def get_safe_phone(driver):
    driver.find_element(By.CLASS_NAME,'btn_text').click()
    i = 0
    while(i < 50):
        sleep(1)
        pdp_soup = BeautifulSoup(driver.page_source, 'html.parser')
        phone = pdp_soup.find('p', {'class':'tell'})
        phone_strip = phone.text.strip()
        if phone_strip != '***-****-****':
            idx = phone_strip.find('0505')
            safe_phone = phone_strip[idx : idx + 13]
            return safe_phone
        i = i + 1

def handle_tempt(alert):
    alert.accept()
    alert.dismiss()
    print("채팅: 일시적 제한")
    sleep(60 * 60)

def handle_chat_full(alert):
    alert.accept()
    alert.dismiss()
    print("채팅: 방 수 초과 ")
    remove_chats(15)
    return 0

def handle_one_minute(alert):
    alert.accept()
    alert.dismiss()
    print("채팅: 1분안에 너무 많은 방 개설")
    sleep(60 * 1)

def open_chat(driver, article_id):
    driver.get(f"https://cafe.naver.com/chocammall?iframe_url_utf8=%2FArticleRead.nhn%253Fclubid%3D20486145%2526page%3D1%2526menuid%3D214%2526boardtype%3DL%2526articleid%3D{article_id}%2526referrerAllArticles%3Dfalse")
    sleep(3)
    driver.switch_to.frame('cafe_main')
    sleep(3)
    driver.find_element(By.CLASS_NAME,'type_chat').click()
    sleep(3)
    try:
        alert = Alert(driver)
        alert_msg = alert.text
        print(alert_msg)
        if alert_msg.find("초과") > -1:
            handle_chat_full(alert)
            open_chat(driver, article_id)
        elif alert_msg.find("일시적") > -1:
            handle_tempt(alert)
            open_chat(driver, article_id)
        elif alert_msg.find("1분") > -1:
            handle_one_minute(alert)
            open_chat(driver, article_id)
    except:
        print('채팅방 열기 성공')
    
def contact_by_chat(driver, article_id):
    open_chat(driver, article_id)
    sleep(1)
    driver.switch_to.window(driver.window_handles[-1])
    sleep(1)
    i = 0
    while(i < 50):
        sleep(1)
        chat_url = driver.current_url
        if chat_url.find('talk') > 0:
            sleep(1)
            k = 0
            while (k < 50):
                sleep(1)
                btn_send = driver.find_element(By.CLASS_NAME,'btn_send')
                if btn_send:
                    btn_send.click()
                k = k + 1
            sleep(1)
            driver.close()
            break
        i = i + 1
    j = 0
    while (j < 50):
        sleep(1)
        driver.switch_to.window(driver.window_handles[0])
        base_url = driver.current_url
        if base_url.find('talk') < 0:
            break
        j = j + 1
    sleep(30)
    return chat_url

def get_pdp_dicts(driver, article_ids):
    pdp_dicts = []
    for article_id in article_ids:
        try:
            pdp_soup_obj = get_pdp_soup(driver, article_id)
        except UnexpectedAlertPresentException as unexpected_alert:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(unexpected_alert).__name__, unexpected_alert.args)
            print(message)
            continue
        if pdp_soup_obj["pdp_soup"] == 'pass':
            continue
        pdp_dict = convert_soup_to_dict(pdp_soup_obj)
        if pdp_dict["phone"] == '***-****-****':
            pdp_dict["phone"] = get_safe_phone(driver)
        pdp_dicts.append(pdp_dict)
    return pdp_dicts