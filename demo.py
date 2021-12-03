from database.database_controller import initial_config
from connection.connection_controller import post_conn

def print_json(json_obj):
    arr_keys=json_obj.keys()
    for index in arr_keys:
        for item in json_obj[index]:
            print(str(item)+" | ")        

initial_config()


