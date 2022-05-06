# -*- coding: utf-8 -*-
import copy
from time import sleep
import requests
import json
from selenium.webdriver.common.by import By
from config import PROFIT

def send_chat(driver, phone):
    driver.get(phone)
    i = 0
    while (i < 50):
        sleep(0.1)
        btn_send = driver.find_element(By.CLASS_NAME,'btn_send')
        if btn_send:
            btn_send.click()
        i = i + 1
    sleep(1)

def send_msg(phone, article_id):
    send_url = 'https://apis.aligo.in/send/' 
    sms_data={'key': 'lojil01d9l07fj51lllttduubepsvwzf', #api key
            'userid': 'oden0317', # 알리고 사이트 아이디
            'sender': '01071416956', # 발신번호
            'receiver': f'{phone}', # 수신번호 (,활용하여 1000명까지 추가 가능)
            # 'receiver': '01099712502', # 수신번호 (,활용하여 1000명까지 추가 가능)
            'msg': f'상품에 관심있어 연락드려요.https://cafe.naver.com/chocammall/{article_id}', #문자 내용 
            'msg_type' : 'msg_type', #메세지 타입 (SMS, LMS)
            #'rdate' : '예약날짜',
            #'rtime' : '예약시간',
            #'testmode_yn' : '' #테스트모드 적용 여부 Y/N
    }
    send_response = requests.post(send_url, data=sms_data)
    print (send_response.json())

def send_reserve(dict, driver, profit):
    phone = dict['phone']
    article_id = dict['article_id']
    if dict['profit']:
        if dict['profit'] > profit:
            if phone.find('talk') > 0:
                send_chat(driver, phone)
                print('reserved with chat')
            else:
                phone_remove_hypen = phone.replace('-','')
                send_msg(phone_remove_hypen, article_id)
                print('reserved with msg')
            dict['reserve'] = 100
    else:
        dict['reserve'] = 200

def send_reserve_all(driver, dicts_calculated, reserve):
    dicts_reserved = []
    for dict_calculated in dicts_calculated:
        dict_reserved = copy.deepcopy(dict_calculated)
        dict_reserved['reserve'] = 0
        if reserve:
            send_reserve(dict_reserved, driver, PROFIT)
        dicts_reserved.append(dict_reserved)
    return dicts_reserved
        