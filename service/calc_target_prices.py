def calc_price_with_model(model, service_fee):
    model_name = model['model_name']
    fair_price = model['fair_price']
    if fair_price:
        target_price = fair_price - service_fee
    else:
        target_price = None
    price_with_model = dict(model=model_name, price=target_price)
    return price_with_model


def calc_target_prices(keywords_models, service_fee):
    prices_with_model = []
    for model in keywords_models:
        price_with_model = calc_price_with_model(model, service_fee)
        prices_with_model.append(price_with_model)
    return prices_with_model