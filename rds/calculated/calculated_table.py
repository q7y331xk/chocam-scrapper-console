from rds.rds import conn_db

def create_calculated_table_if_exists_drop(calculated_table):
    conn = conn_db()
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {calculated_table}")
    cursor.execute(f"CREATE TABLE {calculated_table} (\
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
        `profit` TEXT\
    )")
    conn.commit()

def write_calculated_table(calculated_dicts, calculated_table):
    conn = conn_db()
    cursor = conn.cursor()
    for calculated_dict in calculated_dicts:
        cursor.execute(f"INSERT INTO {calculated_table} VALUES(\
            \"{id}\",\
            \"{calculated_dict['article_id']}\",\
            \"{calculated_dict['title']}\",\
            \"{calculated_dict['cost']}\",\
            \"{calculated_dict['nickname']}\",\
            \"{calculated_dict['status']}\",\
            \"{calculated_dict['use_cnt']}\",\
            \"{calculated_dict['condition']}\",\
            \"{calculated_dict['pay_methods']}\",\
            \"{calculated_dict['delivery']}\",\
            \"{calculated_dict['location']}\",\
            \"{calculated_dict['main']}\",\
            \"{calculated_dict['views']}\",\
            \"{calculated_dict['date']}\",\
            \"{calculated_dict['likes']}\",\
            \"{calculated_dict['comments_cnt']}\",\
            \"{calculated_dict['comments']}\",\
            \"{calculated_dict['phone']}\",\
            \"{calculated_dict['div']}\",\
            \"{calculated_dict['gu']}\",\
            \"{calculated_dict['color']}\",\
            \"{calculated_dict['brand']}\",\
            \"{calculated_dict['model']}\",\
            \"{calculated_dict['jangbak']}\",\
            \"{calculated_dict['grade']}\",\
            \"{calculated_dict['limited']}\",\
            \"{calculated_dict['groundsheet']}\",\
            \"{calculated_dict['inner_tent']}\",\
            \"{calculated_dict['urethane']}\",\
            \"{calculated_dict['vestibule']}\",\
            \"{calculated_dict['set']}\",\
            \"{calculated_dict['profit']}\"\
        )")
    conn.commit()