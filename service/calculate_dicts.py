import copy

def find_model_target_price(model_name, target_prices):
    model_prices = dict(filter_price=None, fair_price=None)
    for target_price in target_prices:
        if model_name == target_price['model']:
            model_prices['filter_price'] = target_price['price']
            model_prices['fair_price'] = target_price['price']
            break
    return model_prices

def calculate_datum(dict_processed, target_prices):
    dict_calculated = copy.deepcopy(dict_processed)
    target_prices = find_model_target_price(dict_calculated['model'],target_prices)
    fair_price = None
    profit = None
    target_price = target_prices['filter_price']
    fair_price = target_prices['fair_price']
    if target_price:
        profit = target_price - dict_calculated['cost']
    dict_calculated['fair_price'] = fair_price
    dict_calculated['profit'] = profit
    return dict_calculated

def calculate_dicts(dicts_processed, target_prices):
    dicts_calculated = []
    for dict_processed in dicts_processed:
        dicts_calculated.append(calculate_datum(dict_processed, target_prices))
    return dicts_calculated