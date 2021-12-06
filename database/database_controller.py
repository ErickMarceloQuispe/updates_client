import sqlite3
import database.initial_querys as InitSql
from connection.connection_controller import post_conn

DB_NAME="database/test_client.db"

def process_sql_sentences(sql_sentences):
    if(type(sql_sentences)==str):
        sql_sentences=sql_sentences.split(";")
    return sql_sentences

def execute_sql_sentences(sql_sentences):
    try:
        sql_sentences=process_sql_sentences(sql_sentences)
        conn = sqlite3.connect(DB_NAME)
        c=conn.cursor()
        results=[]
        for sql_sentence in sql_sentences:
            print(sql_sentence)
            c.execute(sql_sentence)
            for item in c.fetchall():
                results.append(item)
        return results
    except sqlite3.IntegrityError as e:
        return ["Posible repetición de Primary Key"]
    except Exception as e:
        return [str(e)]
    finally:
        conn.commit()
        conn.close
    

def initial_config():
    exist_main_tables=execute_sql_sentences(InitSql.updates_exists)
    if(len(exist_main_tables)==0):
        execute_sql_sentences(InitSql.first_build)
        execute_sql_sentences(post_conn("http://localhost:5000/build-sql-id",{"build_id":1}))
    date_query_res=execute_sql_sentences(InitSql.get_last_update_date)
    print("fecha: "+str (date_query_res) )
    if(date_query_res==[]):
        print(execute_sql_sentences("INSERT INTO builds(description) VALUES ('Dummy Build')"))
        print(execute_sql_sentences (post_conn("http://localhost:5000/build-sql-date",{"last_update_date":"2000-01-01 00:00:00"})) )
    else:
        execute_sql_sentences(post_conn("http://localhost:5000/build-sql-date",{"last_update_date":date_query_res[0][0]}))
    run_downloaded()

def run_downloaded():
    sql_sentences=(execute_sql_sentences("""
    SELECT sql_sentence FROM sql_sentences where sql_sentence_id in 
        ( select sql_sentence_id from change_sql_sentences where change_id in 
            (SELECT change_id FROM changes WHERE update_id IN 
                (SELECT update_id from updates where status='Downloaded' ORDER BY created_at) ORDER BY sequence) ORDER BY sequence
        );"""))
    for item in sql_sentences:
        execute_sql_sentences(item[0].replace("`","'"))
    execute_sql_sentences("UPDATE updates SET status='Installed' WHERE status='Downloaded';")