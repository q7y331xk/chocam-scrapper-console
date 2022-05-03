from config import EXCEL_KEYWORDS_PATH, NEW_TABLE, RDS_TABLE, SILENCE
from excel.import_keywords import import_keywords
from scrapping.scrapping import get_article_ids, get_pdp_dicts
from rds.rds import write_db, conn_db, create_table_if_exists_drop
from auth.auth import naver_login, set_cookies
from service.find_new_article import find_new_article_ids
from service.process_dict import process_dicts

# change id and pw

def write(table, new_table):
    print("========================================")
    print("check crawling options")
    if new_table:
        print('crawl into new table')
        create_table_if_exists_drop(table)
    else:
        print('crawl into exist table')
    if SILENCE:
        print('without opening browser')
    print("========================================")
    keywords = import_keywords(EXCEL_KEYWORDS_PATH)
    login = naver_login(SILENCE)
    driver = login['driver']
    cookies = login['cookies']
    req_session = set_cookies(cookies)
    while(True):
        new_ids = find_new_article_ids(driver, table)
        if new_ids == []:
            continue
        new_pdp_dicts = get_pdp_dicts(driver, new_ids)
        dicts_processed = process_dicts(new_pdp_dicts, keywords)
        # save_and_send_msg(table, new_pdp_dicts)
        # if new? save and start process
    # pdp_dicts = get_pdp_dicts(driver)
    # write_db(pdp_dicts)
    print("done")

write(RDS_TABLE, NEW_TABLE)