import copy
from service.sub_process_dict import extract_brand_model, extract_cost, extract_details, extract_div, extract_grade, extract_groundsheet, extract_gu, extract_inner_tent, extract_jangbak, extract_limited, extract_set, extract_status, extract_urethane, extract_use_cnt, extract_vestibule, extract_color

def process_raw_datum(pdp_dict):
    extract_details(pdp_dict)
    return pdp_dict

def process_datum(raw_datum, keywords):
    processed_datum = copy.deepcopy(raw_datum)
    extract_cost(processed_datum)
    extract_status(processed_datum)
    extract_use_cnt(processed_datum)
    extract_brand_model(keywords["models"], processed_datum, '.')
    extract_jangbak(processed_datum, 0)
    extract_grade(processed_datum)
    extract_limited(keywords['limited'], processed_datum)
    extract_groundsheet(keywords['groundsheet'], processed_datum)
    extract_inner_tent(keywords['inner_tent'], processed_datum)
    extract_urethane(keywords["urethane"], processed_datum)
    extract_vestibule(keywords["vestibule"], processed_datum)
    extract_set(keywords["set"], processed_datum)
    extract_div(keywords["divs"], processed_datum)
    extract_gu(keywords["gus"], processed_datum)
    extract_color(keywords["colors"], processed_datum)
    return processed_datum

def process_dicts(raw_dicts, keywords):
    converted_dicts = []
    for raw_dict in raw_dicts:
        converted_dicts.append(process_datum(raw_dict, keywords))
    return converted_dicts