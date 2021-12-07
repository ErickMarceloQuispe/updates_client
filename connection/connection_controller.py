import requests
import json

#Envia una solicitud POST al URL indicado, con los argumentos en el JSON también indicado
#Retorna un arreglo
def post_conn(url,args_json):
    response = requests.post(url,args_json)
    json_response=json.loads(response.text)
    return json_to_arr(json_response)

#Convierte un objeto Json a un Arreglo, donde solo se toman en cuenta los valores
def json_to_arr(json_obj):
    arr_keys=json_obj.keys()
    results=[]
    for index in arr_keys:
        results.append(str(json_obj[index]))
    return results