from datetime import datetime
from time import strftime

# 현재 챗은 CHAT_RESERVE = False로 막아둠
# 구매 예약 문자는 다 내폰으로

# 어떤 키워드들은 variables.py에 있다.
# OPTIONS
OPTION_NEW_TABLE = False
SILENCE = False
CHAT_RESERVE = True
SERVICE_FEE = 0
PROFIT = 0
RESERVE = True  # filter reserve
CONTACT = True  # send reserve
SENDER_PHONE = '01071416956'
TODAY = datetime.today().strftime('%Y%m%d')

# RDS
RDS_HOST = 'oden-second-hands-selling.ctj9mgachfi3.ap-northeast-2.rds.amazonaws.com'
RDS_USER_NAME = 'admin'
RDS_USER_PW = 'pLa5yfCbS^rCt^vh'
RDS_DB = 'chocam'
RDS_RAW_TABLE = 'current_raw'
RDS_PROCESSED_TABLE = 'current_processed'
RDS_CALCULATED_TABLE = 'current_calculated'
RDS_RESERVED_TABLE = 'current_reserved'

# EXCEL
EXCEL_FILE_NAME = f'current_reserved_{TODAY}'
EXCEL_SAVE_PATH = f"/Users/duckyounglee/Documents/{EXCEL_FILE_NAME}.xlsx"
EXCEL_KEYWORDS_NAME = 'keywords_220524_1030'
EXCEL_KEYWORDS_PATH = f"/Users/duckyounglee/Documents/keywords/{EXCEL_KEYWORDS_NAME}.xlsx"

# Naver Login
NAVER_ID = 'oden0317'
NAVER_PW = 'Dhems2021!'

# telegram
TELE_API_KEY = "5362630249:AAHPegjrSozzmEUlL_DQGlfJ-Roccmm7Cd4"
CHAT_ID_PRIORITY_ONE = "-1001660821686"
CHAT_ID_PRIORITY_TWO = "-1001507095114"