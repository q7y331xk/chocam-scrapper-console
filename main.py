from config import CHAT_ID_PRIORITY_ONE, EXCEL_KEYWORDS_PATH, OPTION_NEW_TABLE, RDS_CALCULATED_TABLE, RDS_PROCESSED_TABLE, RDS_RAW_TABLE, RDS_RESERVED_TABLE, RESERVE, SERVICE_FEE, SILENCE
from create_new_tables import create_tables_if_exists_drop
from excel.import_keywords import import_keywords
from rds.calculated.calculated_table import write_calculated_table
from rds.processed.processed_table import write_processed_table
from rds.raw.raw_table import write_raw_table
from rds.reserved.reserved_table import write_reserved_table
from scrapping.scrapping import get_pdp_dicts
from auth.auth import naver_login, set_cookies
from service.calc_target_prices import calc_target_prices
from service.calculate_dicts import calculate_dicts
from service.find_new_article import find_new_article_ids
from service.process_dicts import process_dicts
from service.raw_dicts import minimum_dicts
from service.send_reserve import send_reserve_all, tele

# change id and pw

def write(raw_table, processed_table, calculated_table, reserved_table, option_new_table):
    print("========================================")
    print("check crawling options")
    if option_new_table:
        print('crawl into new table')
        create_tables_if_exists_drop(raw_table, processed_table, calculated_table, reserved_table)
    else:
        print('crawl into exist table')
    if SILENCE:
        print('without opening browser')
    print("========================================")
    keywords = import_keywords(EXCEL_KEYWORDS_PATH)
    target_prices = calc_target_prices(keywords['models'], SERVICE_FEE)
    login = naver_login(SILENCE)
    driver = login['driver']
    while(True):
        new_ids = find_new_article_ids(driver, raw_table)
        if new_ids == []:
            continue
        new_pdp_dicts = get_pdp_dicts(driver, new_ids)
        raw_dicts = minimum_dicts(new_pdp_dicts)
        write_raw_table(raw_dicts, raw_table)
        dicts_processed = process_dicts(raw_dicts, keywords)
        write_processed_table(dicts_processed, processed_table)
        dicts_calculated = calculate_dicts(dicts_processed, target_prices)
        write_calculated_table(dicts_calculated, calculated_table)
        dicts_reserved = send_reserve_all(driver, dicts_calculated, keywords, RESERVE)
        write_reserved_table(dicts_reserved, reserved_table)
        print('added')

def restart_if_error():
    while(True):
        try:
            tele(CHAT_ID_PRIORITY_ONE, "크롤링 시작")
            write(RDS_RAW_TABLE, RDS_PROCESSED_TABLE, RDS_CALCULATED_TABLE, RDS_RESERVED_TABLE, OPTION_NEW_TABLE)
        except KeyboardInterrupt as error:
            tele(CHAT_ID_PRIORITY_ONE, "의도된 크롤링 종료")
            print("keybord: ", error)
            break
        except Exception:
            print(Exception)
            tele(CHAT_ID_PRIORITY_ONE, "오류로 인한 크롤링 종료")

restart_if_error()
# write(RDS_RAW_TABLE, RDS_PROCESSED_TABLE, RDS_CALCULATED_TABLE, RDS_RESERVED_TABLE, OPTION_NEW_TABLE)