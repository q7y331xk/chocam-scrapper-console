import pymysql
from config import RDS_HOST, RDS_USER_NAME, RDS_USER_PW, RDS_DB, RDS_RAW_TABLE, EXCEL_RDS_READ_TABLE

def conn_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    return conn

def read_db():
    conn = pymysql.connect(host=RDS_HOST, user=RDS_USER_NAME, password=RDS_USER_PW, charset='utf8', port=3306, db=RDS_DB)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {EXCEL_RDS_READ_TABLE}")
    sellings = cursor.fetchall()
    conn.commit()
    return sellings