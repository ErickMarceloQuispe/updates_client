import sqlite3
import database.initial_querys as InitSql

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
    except sqlite3.IntegrityError:
        return ["Posible repetición de Primary Key"]
    except Exception as e:
        return [str(e)]
    finally:
        conn.commit()
        conn.close
    

def initial_config():
    exist_main_tables=execute_sql_sentences(InitSql.updates_exists)
    if(len(exist_main_tables)==0):
        print("NO EXISTE")


def run_build(build_id):
    results=execute_sql_sentences(get_build_sql_sentences(build_id))
    return results

#TO CLIENT
# def update_needs_query(date):
#     sql_sentence="" 
#     if(date!=None):
#         sql_sentence="""select * from updates where created_at > %s order by created_at;
#                     select * from updates order by created_at;"""%date
#     else:
#         sql_sentence="select * from updates order by created_at;"
#     results=execute_sql_sentences([sql_sentence])
#     print(results)

# def get_build_sql_sentences(build_id):
#     sql_sentence="""SELECT sql_sentence from sql_sentences where sql_sentence_id in 
#                 (SELECT sql_sentence_id from build_sql_sentences where build_id = %s ORDER By sequence desc)"""%build_id
#     results=execute_sql_sentences([sql_sentence])
#     build_sql_sentences=[]
#     for item in results:
#         build_sql_sentences.append(item[0])
#     return build_sql_sentences