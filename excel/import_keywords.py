import openpyxl

def import_models(wb):
    models = []
    ws = wb['models']
    rows = ws.rows
    for row in rows:
        model = {}
        brand = row[0].value
        model_name = row[1].value
        additional_keywords_str = row[2].value
        if additional_keywords_str:
            additional_keywords = additional_keywords_str.split(',')
        else:
            additional_keywords = additional_keywords_str
        if model_name:
            model = dict(brand=brand, model_name=model_name, additional_keywords=additional_keywords)
            models.append(model)
    return models

def import_divs(wb):
    divs = []
    ws = wb['divs']
    rows = ws.rows
    for row in rows:
        divs.append(row[0].value)
    return divs

def import_gus(wb):
    gus = []
    ws = wb['gus']
    rows = ws.rows
    for row in rows:
        gus.append(row[0].value)
    return gus

def import_colors(wb):
    colors = []
    ws = wb['colors']
    rows = ws.rows
    for row in rows:
        colors.append(row[0].value)
    return colors

def import_limited(wb):
    limited = []
    ws = wb['limited']
    rows = ws.rows
    for row in rows:
        limited.append(row[0].value)
    return limited

def import_groundsheet(wb):
    groundsheet = []
    ws = wb['groundsheet']
    rows = ws.rows
    for row in rows:
        groundsheet.append(row[0].value)
    return groundsheet

def import_inner_tent(wb):
    inner_tent = []
    ws = wb['inner_tent']
    rows = ws.rows
    for row in rows:
        inner_tent.append(row[0].value)
    return inner_tent

def import_urethane(wb):
    urethane = []
    ws = wb['urethane']
    rows = ws.rows
    for row in rows:
        urethane.append(row[0].value)
    return urethane

def import_vestibule(wb):
    vestibule = []
    ws = wb['vestibule']
    rows = ws.rows
    for row in rows:
        vestibule.append(row[0].value)
    return vestibule

def import_set(wb):
    set = []
    ws = wb['set']
    rows = ws.rows
    for row in rows:
        set.append(row[0].value)
    return set

def import_keywords(excel_keywords_path):
    keywords = {}
    wb = openpyxl.load_workbook(excel_keywords_path)
    keywords["models"] = import_models(wb)
    keywords["divs"] = import_divs(wb)
    keywords["gus"] = import_gus(wb)
    keywords["colors"] = import_colors(wb)
    keywords["limited"] = import_limited(wb)
    keywords["groundsheet"] = import_groundsheet(wb)
    keywords["inner_tent"] = import_inner_tent(wb)
    keywords["urethane"] = import_urethane(wb)
    keywords["vestibule"] = import_vestibule(wb)
    keywords["set"] = import_set(wb)
    return keywords