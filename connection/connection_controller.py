import requests
import json

def post_conn(url,args_json):
    response = requests.post(url,args_json)
    json_response=json.loads(response.text)
    print_json(json_response)


# url="http://localhost:5000/sql"
# _json = {"sql_sentence":
#         """SELECT sql_sentence FROM sql_sentences where sql_sentence_id in (
#         select sql_sentence_id from change_sql_sentences where change_id in 
#         (select change_id from changes where update_id="v1.3" order by changes.sequence) 
#         ORDER BY change_sql_sentences.sequence);"""
# }