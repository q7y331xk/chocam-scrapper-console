from str.string import match_keywords
from variables import MAIN_BUY_KEYWORDS, MAIN_NEW_KEYWORDS, TITLE_BUY_KEYWORDS, TITLE_NEW_KEYWORDS
import re

def extract_cost(processed_datum):
    cost_significant = check_cost_significant(processed_datum['cost'])
    if not cost_significant:
        processed_datum['cost'] = main_find_cost(processed_datum['main'])
    return processed_datum

def extract_details(pdp_converted):
    pdp_converted['condition'] = ''
    pdp_converted['pay_methods'] = ''
    pdp_converted['delivery'] = ''
    pdp_converted['location'] = ''
    details = pdp_converted['details']
    for detail in details:
        for key, value in detail.items():
            if key == '상품 상태':
                pdp_converted['condition'] = value
            if key == '결제 방법':
                pdp_converted['pay_methods'] = value
            if key == '배송 방법':
                pdp_converted['delivery'] = value
            if key == '거래 지역':
                pdp_converted['location'] = value
    del(pdp_converted['details'])
    return pdp_converted

def check_cost_significant(cost_int):
    significant = True
    cost_text = str(cost_int)
    if cost_text.find('123') > -1:
        significant = False
    if cost_text.replace(cost_text[0],'') == '':
        significant = False
    if cost_int < 10000:
        significant = False
    if cost_int > 9000000:
        significant = False
    return significant

def main_find_cost(main_text):
    found_cost = -1
    find_num_won = re.search(r"[0-9]+원", main_text)
    find_num_man = re.search(r"[0-9]+만", main_text)
    if find_num_won:
        found_cost = int(find_num_won.group().replace('원',''))
    if find_num_man:
        found_cost = int(find_num_man.group().replace('만','')) * 10000
    return found_cost

def is_status_exchange(processed_datum):
    found_in_title = re.search('교환',processed_datum['title'])
    if found_in_title:
        return True
    return False

def is_status_buy(processed_datum):
    if match_keywords(processed_datum['title'], TITLE_BUY_KEYWORDS):
        return True
    if match_keywords(processed_datum['main'], MAIN_BUY_KEYWORDS):
        return True
    return False

def extract_status(processed_datum):
    if is_status_exchange(processed_datum):
        processed_datum['status'] = '교환'
    if is_status_buy(processed_datum):
        processed_datum['status'] = '구매'

def extract_use_cnt(processed_datum):
    title = processed_datum['title']
    main = processed_datum['main']
    if processed_datum['condition'] == '미개봉':
        processed_datum['use_cnt'] = 0
        return 
    if match_keywords(title, TITLE_NEW_KEYWORDS):
        processed_datum['use_cnt'] = 0
        return
    if match_keywords(main, MAIN_NEW_KEYWORDS):
        processed_datum['use_cnt'] = 0
        return
    found_hoe = re.search(r"[0-9]+회", main)
    if found_hoe:
        processed_datum['use_cnt'] = int(found_hoe.group().replace('회', ''))
        return
    found_bun = re.search(r"[0-9]+번", main)
    if found_bun:
        processed_datum['use_cnt'] = int(found_bun.group().replace('번', ''))
        return
    if match_keywords(main, ['한번']):
        processed_datum['use_cnt'] = 1
        return
    if match_keywords(main, ['두번']):
        processed_datum['use_cnt'] = 2
        return
    if match_keywords(main, ['세번']):
        processed_datum['use_cnt'] = 3
        return
    return -1

def extract_brand_model(models, processed_datum, default=None):
    brand = default
    model_name = default
    for model in models:
        if model["additional_keywords"]:
            keywords = [model["model_name"]] + model["additional_keywords"]
        else:
            keywords = [model["model_name"]]
        model_found = match_keywords(processed_datum['title'].replace(' ',''), keywords, default)
        if model_found != default:
            brand = model["brand"]
            model_name = model["model_name"]
            break
    processed_datum["brand"] = brand
    processed_datum["model"] = model_name

def extract_jangbak(processed_datum, default):
    jangbak = default
    main = processed_datum['main']
    main_converted = main.replace(' ', '').upper().replace('포장박스', '').replace('장박용', '').replace('장박없', '').replace('장박X', '').replace('장박이력없', '')
    found = re.search('장박', main_converted)
    if found:
        jangbak = 1
    processed_datum["jangbak"] = jangbak


def extract_limited(keywords_limited, processed_datum):
    title = processed_datum["title"]
    limited = 0
    if match_keywords(title, keywords_limited):
        limited = 1
    processed_datum["limited"] = limited

def extract_groundsheet(keywords_groundsheet, processed_datum):
    title = processed_datum["title"]
    main = processed_datum['main']
    groundsheet = 0
    if match_keywords(title, keywords_groundsheet):
        groundsheet = 1
    elif match_keywords(main, keywords_groundsheet):
        groundsheet = 1
    processed_datum["groundsheet"] = groundsheet

def extract_inner_tent(keywords_inner_tent, processed_datum):
    title = processed_datum["title"]
    main = processed_datum['main']
    inner_tent = 0
    if match_keywords(title.replace("라이너","").replace("이너매트","").replace("이너메트",""), keywords_inner_tent):
        inner_tent = 1
    elif match_keywords(main.replace("라이너","").replace("이너매트","").replace("이너메트",""), keywords_inner_tent):
        inner_tent = 1
    processed_datum["inner_tent"] = inner_tent
    
def extract_urethane(keywords_urethane, processed_datum):
    title = processed_datum["title"]
    main = processed_datum['main']
    urethane = 0
    if match_keywords(title, keywords_urethane):
        urethane = 1
    elif match_keywords(main, keywords_urethane):
        urethane = 1
    processed_datum["urethane"] = urethane

def extract_vestibule(keywords_vestibule, processed_datum):
    title = processed_datum["title"]
    main = processed_datum['main']
    vestibule = 0
    if match_keywords(title, keywords_vestibule):
        vestibule = 1
    elif match_keywords(main, keywords_vestibule):
        vestibule = 1
    processed_datum["vestibule"] = vestibule

def extract_set(keywords_set, processed_datum):
    title = processed_datum["title"]
    main = processed_datum['main']
    set = 0
    if processed_datum['groundsheet'] or processed_datum['inner_tent'] or processed_datum['urethane'] or processed_datum['vestibule']:
        set = 1
    else:
        if match_keywords(title, keywords_set):
            set = 1
        elif match_keywords(main, keywords_set):
            set = 1
    processed_datum["set"] = set