from config import RDS_CALCULATED_TABLE, RDS_PROCESSED_TABLE, RDS_RAW_TABLE, RDS_RESERVED_TABLE
from rds.calculated.calculated_table import create_calculated_table_if_exists_drop
from rds.processed.processed_table import create_processed_table_if_exists_drop
from rds.raw.raw_table import create_raw_table_if_exists_drop
from rds.reserved.reserved_table import create_reserved_table_if_exists_drop

def create_tables_if_exists_drop(raw_table, processed_table, calculated_table, reserved_table):
    create_raw_table_if_exists_drop(raw_table)
    create_processed_table_if_exists_drop(processed_table)
    create_calculated_table_if_exists_drop(calculated_table)
    create_reserved_table_if_exists_drop(reserved_table)