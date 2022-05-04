from rds.rds import conn_db

def create_raw_table_if_exists_drop(raw_table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {raw_table}")
    cursor.execute(f"CREATE TABLE {raw_table} (\
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,\
        article_id INT,\
        title TEXT,\
        cost INT,\
        nickname TEXT,\
        `status` TEXT,\
        `condition` TEXT,\
        pay_methods TEXT,\
        delivery TEXT,\
        location TEXT,\
        main TEXT,\
        views INT,\
        date DATETIME,\
        likes TEXT,\
        comments_cnt INT,\
        comments TEXT\
    )")
    conn.commit()

def write_raw_table(raw_dicts, raw_table):
    conn = conn_db()
    cursor = conn.cursor()
    for raw_dict in raw_dicts:
        cursor.execute(f"INSERT INTO {raw_table} VALUES(\
            \"{id}\",\
            \"{raw_dict['article_id']}\",\
            \"{raw_dict['title']}\",\
            \"{raw_dict['cost']}\",\
            \"{raw_dict['nickname']}\",\
            \"{raw_dict['status']}\",\
            \"{raw_dict['condition']}\",\
            \"{raw_dict['pay_methods']}\",\
            \"{raw_dict['delivery']}\",\
            \"{raw_dict['location']}\",\
            \"{raw_dict['main']}\",\
            \"{raw_dict['views']}\",\
            \"{raw_dict['date']}\",\
            \"{raw_dict['likes']}\",\
            \"{raw_dict['comments_cnt']}\",\
            \"{raw_dict['comments']}\"\
        )")
    conn.commit()

def get_recent_fromDB(table, limits):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} ORDER BY id DESC LIMIT {limits}")
    rows = cursor.fetchall()
    conn.commit()
    return rows
