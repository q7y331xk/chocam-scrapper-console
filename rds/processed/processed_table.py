from rds.rds import conn_db

def create_processed_table_if_exists_drop(processed_table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {processed_table}")
    cursor.execute(f"CREATE TABLE {processed_table} (\
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
        date DATETIME,\
        likes TEXT,\
        comments_cnt INT,\
        comments TEXT,\
        phone TEXT,\
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

def write_processed_table(processed_dicts, processed_table):
    conn = conn_db()
    cursor = conn.cursor()
    for processed_dict in processed_dicts:
        cursor.execute(f"INSERT INTO {processed_table} VALUES(\
            \"{id}\",\
            \"{processed_dict['article_id']}\",\
            \"{processed_dict['title']}\",\
            \"{processed_dict['cost']}\",\
            \"{processed_dict['nickname']}\",\
            \"{processed_dict['status']}\",\
            \"{processed_dict['use_cnt']}\",\
            \"{processed_dict['condition']}\",\
            \"{processed_dict['pay_methods']}\",\
            \"{processed_dict['delivery']}\",\
            \"{processed_dict['location']}\",\
            \"{processed_dict['main']}\",\
            \"{processed_dict['views']}\",\
            \"{processed_dict['date']}\",\
            \"{processed_dict['likes']}\",\
            \"{processed_dict['comments_cnt']}\",\
            \"{processed_dict['comments']}\",\
            \"{processed_dict['phone']}\",\
            \"{processed_dict['div']}\",\
            \"{processed_dict['gu']}\",\
            \"{processed_dict['color']}\",\
            \"{processed_dict['brand']}\",\
            \"{processed_dict['model']}\",\
            \"{processed_dict['jangbak']}\",\
            \"{processed_dict['grade']}\",\
            \"{processed_dict['limited']}\",\
            \"{processed_dict['groundsheet']}\",\
            \"{processed_dict['inner_tent']}\",\
            \"{processed_dict['urethane']}\",\
            \"{processed_dict['vestibule']}\",\
            \"{processed_dict['set']}\"\
        )")
    conn.commit()