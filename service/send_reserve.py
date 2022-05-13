# -*- coding: utf-8 -*-
import copy
from time import sleep
import requests
import json
from selenium.webdriver.common.by import By
from config import CHAT_ID_PRIORITY_ONE, CHAT_ID_PRIORITY_TWO, CONTACT, SENDER_PHONE
from scrapping.scrapping import contact_by_chat
from variables import SEOUL_GUS
from config import TELE_API_KEY
import telegram


def reserve_chat(driver, article_id):
    chat_url = contact_by_chat(driver, article_id)
    return chat_url

def reserve_msg(phone, article_id):
    send_url = 'https://apis.aligo.in/send/' 
    sms_data={'key': 'lojil01d9l07fj51lllttduubepsvwzf', #api key
            'userid': 'oden0317', # 알리고 사이트 아이디
            'sender': SENDER_PHONE, # 발신번호
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

def notice_chat(phone, article_id, dict, contact, chat_id):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    model_text = dict['text']
    fair_price = dict['fair_price']
    contact_text = "X"
    if contact:
        contact_text = "O"
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    if model_text == '':
        text = f'모델명: {model}({grade})\n게시 금액: {cost}\n적정 금액: {fair_price}\n연락: {contact_text}\n제품 링크: {link}\n채팅 링크: {phone}'
    else:
        text = f'모델명: {model}({grade})\n게시 금액: {cost}\n적정 금액: {fair_price}\n연락: {contact_text}\n제품 링크: {link}\n채팅 링크: {phone}\n{model_text}'
    
    tele(chat_id, text)

def notice_msg(phone, article_id, dict, contact, chat_id):
    model = dict['model']
    grade = dict['grade']
    cost = dict['cost']
    model_text = dict['text']
    fair_price = dict['fair_price']
    contact_text = "X"
    if contact:
        contact_text = "O"
    link = f'https://cafe.naver.com/chocammall/{article_id}'
    if model_text == '':
        text = f'모델명: {model}({grade})\n금액: {cost}\n적정 금액: {fair_price}\n연락: {contact_text}\n제품 링크: {link}\n휴대폰 번호: {phone}'
    else:
        text = f'모델명: {model}({grade})\n금액: {cost}\n적정 금액: {fair_price}\n연락: {contact_text}\n제품 링크: {link}\n휴대폰 번호: {phone}\n{model_text}'
    tele(chat_id, text)

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

def match_priority(model, keywords_models):
    priority = -1
    for keywords_model in keywords_models:
        if keywords_model['model_name'] == model:
            if keywords_model['priority']:
                priority = keywords_model['priority']
            break
    return priority

def match_min_price(model, keywords_models):
    min_price = -1
    for keywords_model in keywords_models:
        if keywords_model['model_name'] == model:
            if keywords_model['min_price']:
                min_price = keywords_model['min_price']
            break
    return min_price

def match_max_price(model, keywords_models):
    max_price = -1
    for keywords_model in keywords_models:
        if keywords_model['model_name'] == model:
            if keywords_model['max_price']:
                max_price = keywords_model['max_price']
            break
    return max_price

def match_text(model, keywords_models):
    text = ""
    for keywords_model in keywords_models:
        if keywords_model['model_name'] == model:
            if keywords_model['text']:
                text = keywords_model['text'].replace('\\n','\n')
            break
    return text

def send_reserve(driver, dict):
    phone = dict['phone']
    article_id = dict['article_id']
    if phone.find('chat') == -1:
        phone_remove_hypen = phone.replace('-','')
        reserve_msg(phone_remove_hypen, article_id)
        print('reserved with msg')
    else:
        chat_url = reserve_chat(driver, article_id)
        print('reserved with chat')
        dict['phone'] = chat_url

def send_notice(dict, contact, chat_id):
    phone = dict['phone']
    article_id = dict['article_id']
    if phone.find('talk') == -1:
        phone_remove_hypen = phone.replace('-','')
        notice_msg(phone_remove_hypen, article_id, dict, contact, chat_id)
    else:
        notice_chat(phone, article_id, dict, contact, chat_id)
    return 111

def is_contactable(dict):
    div = dict['div']
    gu = dict['gu']
    contactable = False
    if is_seoul(div, gu, SEOUL_GUS):
        contactable = True
    elif location_unknown(div, gu):
        contactable = True
    return contactable

def reserve_dict(dict, driver, keywords):
    code = 100
    if (code == 100) and (dict['status'] != "판매"):
        code = 401 # not for sale
    if (code == 100) and (not is_contactable(dict)):
        code = 402 # not contactable
    if (code == 100):
        priority = match_priority(dict['model'], keywords['models'])
        dict['max_price'] = match_max_price(dict['model'], keywords['models'])
        dict['min_price'] = match_min_price(dict['model'], keywords['models'])
        dict['text'] = match_text(dict['model'], keywords['models'])
        if priority > -1: 
            code = 110 # in target
            if priority == 1:
                if (dict['cost'] < dict['max_price']) and (dict['cost'] > dict['min_price']):
                    if CONTACT:  # 120 send notice
                        send_reserve(driver, dict)
                        send_notice(dict, True, CHAT_ID_PRIORITY_ONE)
                        code = 120
                    else:   # 121 contactable but not in contact mode
                        send_notice(dict, False, CHAT_ID_PRIORITY_ONE) # send notice 111
                        code = 121 # not contact mode
                else:
                    code = send_notice(dict, False, CHAT_ID_PRIORITY_ONE) # send notice 111
            if priority == 2:
                code = send_notice(dict, False, CHAT_ID_PRIORITY_TWO) # send notice 111
        else:
            code = 403 # not in target
    return code
        

def reserve_dicts(driver, dicts_calculated, keywords, reserve):
    dicts_reserved = []
    for dict_calculated in dicts_calculated:
        dict_reserved = copy.deepcopy(dict_calculated)
        dict_reserved['reserve'] = 0
        if reserve:
            dict_reserved['reserve'] = reserve_dict(dict_reserved, driver, keywords)
        dicts_reserved.append(dict_reserved)
    return dicts_reserved
    