from rds.raw.raw_table import get_recent_fromDB
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

def find_new_article_ids(driver, raw_table):
    scrapped_ids = get_article_ids(driver)
    recent_articles = get_recent_fromDB(raw_table, 15)
    recent_ids = get_ids_from_article(recent_articles)
    exist_idx = find_exist_idx(scrapped_ids, recent_ids)
    new_ids =  scrapped_ids[0 : exist_idx]
    return new_ids