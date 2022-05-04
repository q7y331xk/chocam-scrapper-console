import copy
from service.sub_process_dict import extract_details

def process_raw_datum(pdp_dict):
    minimal_dict = copy.deepcopy(pdp_dict)
    extract_details(minimal_dict)
    return minimal_dict

def minimum_dicts(pdp_dicts):
    minimal_dicts = []
    for pdp_dict in pdp_dicts:
        minimal_dicts.append(process_raw_datum(pdp_dict))
    return minimal_dicts