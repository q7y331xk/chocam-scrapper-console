from rds.rds import read_db
from excel.excel import write_excel, write_exist_excel

sellings = read_db()
write_excel(sellings)