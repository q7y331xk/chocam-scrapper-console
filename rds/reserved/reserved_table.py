from rds.rds import conn_db

def create_reserved_table_if_exists_drop(reserved_table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {reserved_table}")
    cursor.execute(f"CREATE TABLE {reserved_table} (\
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
        `set` TEXT,\
        `profit` TEXT,\
        `reserve` TEXT\
    )")
    conn.commit()

def write_reserved_table(reserved_dicts, reserved_table):
    conn = conn_db()
    cursor = conn.cursor()
    for reserved_dict in reserved_dicts:
        cursor.execute(f"INSERT INTO {reserved_table} VALUES(\
            \"{id}\",\
            \"{reserved_dict['article_id']}\",\
            \"{reserved_dict['title']}\",\
            \"{reserved_dict['cost']}\",\
            \"{reserved_dict['nickname']}\",\
            \"{reserved_dict['status']}\",\
            \"{reserved_dict['use_cnt']}\",\
            \"{reserved_dict['condition']}\",\
            \"{reserved_dict['pay_methods']}\",\
            \"{reserved_dict['delivery']}\",\
            \"{reserved_dict['location']}\",\
            \"{reserved_dict['main']}\",\
            \"{reserved_dict['views']}\",\
            \"{reserved_dict['date']}\",\
            \"{reserved_dict['likes']}\",\
            \"{reserved_dict['comments_cnt']}\",\
            \"{reserved_dict['comments']}\",\
            \"{reserved_dict['phone']}\",\
            \"{reserved_dict['div']}\",\
            \"{reserved_dict['gu']}\",\
            \"{reserved_dict['color']}\",\
            \"{reserved_dict['brand']}\",\
            \"{reserved_dict['model']}\",\
            \"{reserved_dict['jangbak']}\",\
            \"{reserved_dict['grade']}\",\
            \"{reserved_dict['limited']}\",\
            \"{reserved_dict['groundsheet']}\",\
            \"{reserved_dict['inner_tent']}\",\
            \"{reserved_dict['urethane']}\",\
            \"{reserved_dict['vestibule']}\",\
            \"{reserved_dict['set']}\",\
            \"{reserved_dict['profit']}\",\
            \"{reserved_dict['reserve']}\"\
        )")
    conn.commit()