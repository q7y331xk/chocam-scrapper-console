from rds.rds import get_recent_fromDB
from scrapping.scrapping import get_article_ids

def find_exist_idx(new_ids, recent_ids):
    for idx, new_id in enumerate(new_ids):
        count = recent_ids.count(new_id)
        if count:
            return idx
    return 20

def get_ids_from_article(articles):
    ids = []
    for article in articles:
        ids.append(article[1])
    return ids

def find_new_article_ids(driver, table):
    scrapped_ids = get_article_ids(driver)
    recent_articles = get_recent_fromDB(table)
    recent_ids = get_ids_from_article(recent_articles)
    scrapped_ids = [7683380, 7681188, 7681168, 7681138, 7681103, 7681101, 7681100, 7681094, 7681090, 7681087, 7681086, 7681085, 7681081, 7681080, 7681078, 7681077, 7681076, 7681075]
    # recent_ids = [7681103, 7681101, 7681100, 7681094, 7681090, 7681087, 7681086, 7681085, 7681081, 7681080, 7681078, 7681077, 7681076, 7681075]
    recent_ids = [7681100, 7681094, 7681090, 7681087, 7681086, 7681085, 7681081, 7681080, 7681078, 7681077, 7681076, 7681075]
    exist_idx = find_exist_idx(scrapped_ids, recent_ids)
    new_ids =  scrapped_ids[0 : exist_idx]
    return new_ids