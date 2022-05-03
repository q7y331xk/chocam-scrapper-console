import copy
from service.sub_process_dict import extract_brand_model, extract_cost, extract_details, extract_groundsheet, extract_inner_tent, extract_jangbak, extract_limited, extract_set, extract_status, extract_urethane, extract_use_cnt, extract_vestibule

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
    # extract_grade(processed_datum)
    extract_limited(keywords['limited'], processed_datum)
    extract_groundsheet(keywords['groundsheet'], processed_datum)
    extract_inner_tent(keywords['inner_tent'], processed_datum)
    extract_urethane(keywords["urethane"], processed_datum)
    extract_vestibule(keywords["vestibule"], processed_datum)
    extract_set(keywords["set"], processed_datum)
    #### location divs, gus
    print(processed_datum)


def process_dict(pdp_dict, keywords):
    raw_datum = process_raw_datum(pdp_dict)
    #### save here too
    processed_datum = process_datum(raw_datum, keywords)
    return 

def process_dicts(pdp_dicts, keywords):
    converted_dicts = []
    for pdp_dict in pdp_dicts:
        converted_dicts.append(process_dict(pdp_dict, keywords))
    return converted_dicts