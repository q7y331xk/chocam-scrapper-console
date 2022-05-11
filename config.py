# 현재 챗은 CHAT_RESERVE = False로 막아둠
# 구매 예약 문자는 다 내폰으로

# 어떤 키워드들은 variables.py에 있다.
# OPTIONS
OPTION_NEW_TABLE = False
SILENCE = False
CHAT_RESERVE = False
SERVICE_FEE = 0
PROFIT = 0
RESERVE = True # 지금은 테스트용으로 다 나한테 문자오게함
PRODUCT = False 
NOTICE_PHONE = '01071416956'

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
EXCEL_FILE_NAME = 'current_calculated1'
EXCEL_SAVE_PATH = f"/Users/duckyounglee/Documents/{EXCEL_FILE_NAME}.xlsx"
EXCEL_KEYWORDS_NAME = 'keywords'
EXCEL_KEYWORDS_PATH = f"/Users/duckyounglee/Documents/{EXCEL_KEYWORDS_NAME}.xlsx"

# Naver Login
NAVER_ID = 'q7y331xk'
NAVER_PW = 'f7gh18Sh94#'