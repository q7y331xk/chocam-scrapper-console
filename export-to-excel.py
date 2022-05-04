from config import RDS_CALCULATED_TABLE
from rds.rds import read_db
from excel.excel import write_excel

table_data = read_db(RDS_CALCULATED_TABLE)
columns = table_data['columns']
rows = table_data['rows']
write_excel(columns, rows, 'CALCULATED')