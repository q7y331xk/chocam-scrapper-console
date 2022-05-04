import copy

def find_model_target_price(model_name, target_prices):
    target_price_value = None
    for target_price in target_prices:
        if model_name == target_price['model']:
            target_price_value = target_price['price']
            break
    return target_price_value

def calculate_datum(dict_processed, target_prices):
    dict_calculated = copy.deepcopy(dict_processed)
    target_price = find_model_target_price(dict_calculated['model'],target_prices)
    if target_price:
        profit = target_price - dict_calculated['cost']
    else:
        profit = None
    dict_calculated['profit'] = profit
    return dict_calculated

def calculate_dicts(dicts_processed, target_prices):
    dicts_calculated = []
    for dict_processed in dicts_processed:
        dicts_calculated.append(calculate_datum(dict_processed, target_prices))
    return dicts_calculated