updates_exists="pragma table_info(updates)"
get_last_update_date="select created_at from updates order by created_at desc limit 1"
first_build=[
    """PRAGMA foreign_keys = ON;""",
    """DROP TABLE IF EXISTS build_sql_sentences;""",
    """DROP TABLE IF EXISTS builds;""",
    """DROP TABLE IF EXISTS sql_sentences;""",
    """CREATE TABLE builds (
            build_id INTEGER PRIMARY KEY AUTOINCREMENT,
            description varchar(255)
        );""",

    """CREATE TABLE sql_sentences(
            sql_sentence_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sql_sentence BLOB NOT NULL
        );""",

    """CREATE TABLE build_sql_sentences (
            build_id INTEGER NOT NULL,
            sql_sentence_id INTEGER NOT NULL,
            sequence INTEGER NOT NULL,
            FOREIGN KEY (build_id) REFERENCES builds(build_id),
            FOREIGN KEY (sql_sentence_id) REFERENCES sql_sentences(sql_sentence_id)
        );"""]
