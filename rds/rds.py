import pymysql
import copy
import re
from config import RDS_HOST, RDS_USER_NAME, RDS_USER_PW, RDS_DB, RDS_TABLE, EXCEL_RDS_READ_TABLE

def get_recent_fromDB(table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} ORDER BY id DESC LIMIT 15")
    sellings = cursor.fetchall()
    conn.commit()
    return sellings

def conn_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    return conn

def create_table_if_exists_drop(table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute(f"CREATE TABLE {table} (\
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        article_id INT,\
        title TEXT,\
        cost INT,\
        nickname TEXT,\
        `status` TEXT,\
        use_cnt INT,\
        `condition` TEXT,\
        pay_methods TEXT,\
        delivery TEXT,\
        location TEXT,\
        main TEXT,\
        views INT,\
        date TEXT,\
        likes TEXT,\
        comments_cnt INT,\
        comments TEXT,\
        `div` TEXT,\
        `gu` TEXT,\
        `color` TEXT,\
        `brand` TEXT,\
        `model` TEXT,\
        `jangbak` TEXT,\
        `grade` TEXT,\
        `limited` TEXT,\
        `groundsheet` TEXT,\
        `inner_tent` TEXT,\
        `urethane` TEXT,\
        `vestibule` TEXT,\
        `set` TEXT\
    )")
    conn.commit()

def write_db(pdp_dicts):
    conn = conn_db()
    cursor = conn.cursor()
    for pdp_dict in pdp_dicts:
        pdp_converted = covert_data(pdp_dict)
        cursor.execute(f"INSERT INTO {RDS_TABLE} VALUES(\
            \"{id}\",\
            \"{pdp_converted['title']}\",\
            \"{pdp_converted['cost']}\",\
            \"{pdp_converted['nickname']}\",\
            \"{pdp_converted['status']}\",\
            \"{pdp_converted['use_cnt']}\",\
            \"{pdp_converted['condition']}\",\
            \"{pdp_converted['pay_methods']}\",\
            \"{pdp_converted['delivery']}\",\
            \"{pdp_converted['location']}\",\
            \"{pdp_converted['main']}\",\
            \"{pdp_converted['views']}\",\
            \"{pdp_converted['date']}\",\
            \"{pdp_converted['likes']}\",\
            \"{pdp_converted['comments_cnt']}\",\
            \"{pdp_converted['comments']}\"\
        )")
    conn.commit()

def read_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {EXCEL_RDS_READ_TABLE}")
    sellings = cursor.fetchall()
    conn.commit()
    return sellings