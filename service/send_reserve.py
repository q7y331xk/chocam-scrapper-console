# -*- coding: utf-8 -*-
import copy
from time import sleep
import requests
import json
from selenium.webdriver.common.by import By
from config import CHAT_ID_PRIORITY_ONE, CHAT_ID_PRIORITY_TWO, NOTICE_PHONE, PRODUCT, PROFIT
from variables import SEOUL_GUS
from config import TELE_API_KEY
import telegram


def reserve_chat(driver, phone):
    driver.get(phone)
    i = 0
    while (i < 50):
        sleep(0.1)
        btn_send = driver.find_element(By.CLASS_NAME,'btn_send')
        if btn_send:
            btn_send.click()
        i = i + 1
    sleep(1)

def reserve_msg(phone, article_id):
    send_url = 'https://apis.aligo.in/send/' 
    sms_data={'key': 'lojil01d9l07fj51lllttduubepsvwzf', #api key
            'userid': 'oden0317', # 알리고 사이트 아이디
            'sender': '01071416956', # 발신번호
            'receiver': f'{phone}', # 수신번호 (,활용하여 1000명까지 추가 가능)
            'msg': f'상품에 관심있어 연락드려요.https://cafe.naver.com/chocammall/{article_id}', #문자 내용 
            'msg_type' : 'msg_type', #메세지 타입 (SMS, LMS)
    }
    send_response = requests.post(send_url, data=sms_data)
    # print (send_response.json())

def tele(chat_id, text):
    bot = telegram.Bot(token = TELE_API_KEY)
    text = text
    bot.sendMessage(chat_id=chat_id, text=text)

def notice_chat(phone, article_id, dict):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    fair_price = dict['fair_price']
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    text = f'모델명: {model}({grade})\n금액: {cost}\n적정 금액: {fair_price}\n제품 링크: {link}\n채팅 링크: {phone}'
    tele(CHAT_ID_PRIORITY_ONE, text)

def notice_chat2(phone, article_id, dict):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    fair_price = dict['fair_price']
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    text = f'모델명: {model}({grade})\n금액: {cost}\n적정 금액: {fair_price}\n제품 링크: {link}\n채팅 링크: {phone}'
    tele(CHAT_ID_PRIORITY_TWO, text)

def notice_msg(phone, article_id, dict):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    fair_price = dict['fair_price']
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    text = f'모델명: {model}({grade})\n게시 금액: {cost}\n적정 금액: {fair_price}\n제품 링크: {link}\n휴대폰 번호: {phone}'
    tele(CHAT_ID_PRIORITY_TWO, text)

def notice_msg2(phone, article_id, dict):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    fair_price = dict['fair_price']
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    text = f'모델명: {model}({grade})\n게시 금액: {cost}\n적정 금액: {fair_price}\n제품 링크: {link}\n휴대폰 번호: {phone}'
    tele(CHAT_ID_PRIORITY_ONE, text)

def is_seoul(div, gu, seoul_gus):
    seoul = False
    if div == '서울':
        seoul = True
    else:
        if gu in seoul_gus:
            seoul = True
    return seoul

def location_unknown(div, gu):
    unknown = False
    if div == '.' and gu == '.':
        unknown = True
    return unknown

def send_reserve(dict, driver, profit):
    phone = dict['phone']
    article_id = dict['article_id']
    div = dict['div']
    gu = dict['gu']
    status = dict['status']
    if status == "판매":
        if dict['profit']:
            if dict['profit'] > profit + 10000000:
                seoul = is_seoul(div, gu, SEOUL_GUS)
                unknown = location_unknown(div, gu)
                if seoul or unknown:
                    ####
                    if phone.find('talk') > 0:
                        if PRODUCT:
                            reserve_chat(driver, phone)
                        notice_chat2(phone, article_id, dict)
                        print('reserved with chat')
                    else:
                        phone_remove_hypen = phone.replace('-','')
                        if PRODUCT:
                            reserve_msg(phone_remove_hypen, article_id)
                        notice_msg2(phone_remove_hypen, article_id, dict)
                        print('reserved with msg')
                    return 100
                ###
                else:
                    return 301
            elif dict['profit'] > profit:
                seoul = is_seoul(div, gu, SEOUL_GUS)
                unknown = location_unknown(div, gu)
                if seoul or unknown:
                    ####
                    if phone.find('talk') > 0:
                        if PRODUCT:
                            reserve_chat(driver, phone)
                        notice_chat(phone, article_id, dict)
                        print('reserved with chat')
                    else:
                        phone_remove_hypen = phone.replace('-','')
                        if PRODUCT:
                            reserve_msg(phone_remove_hypen, article_id)
                        notice_msg(phone_remove_hypen, article_id, dict)
                        print('reserved with msg')
                    return 100
                ###
                else:
                    return 301
            else:
                return 300 # expensive
        else:
            return 401 # no model fair price
    else:
        return 402 # not for sale

def send_reserve_all(driver, dicts_calculated, reserve):
    dicts_reserved = []
    for dict_calculated in dicts_calculated:
        dict_reserved = copy.deepcopy(dict_calculated)
        dict_reserved['reserve'] = 0
        if reserve:
            dict_reserved['reserve'] = send_reserve(dict_reserved, driver, PROFIT)
        dicts_reserved.append(dict_reserved)
    return dicts_reserved
        