import requests
import json



# a function to get the sesion ID form ActifioSky Api
def get_session_id():
    api_url = "https://10.30.10.3/actifio/session"
    headers1 =  {"Authorization" : "Basic YWRtaW46T3JhbmdlMTIzIQ=="}
    response = requests.post(api_url, headers=headers1, verify=False)
    json_test= response.json()
    return json_test["session_id"]


#return json_test["sessionid"]
#call the function to get seesion id and save it in sessionid variable
sessionid = get_session_id()
#print the session id
print(sessionid)


#api_url1 = "https://34.116.223.174/actifio/api/info/lshost"
#headers2 =  {"Authorization" : "Actifio "+ sessionid }
#response1 = requests.get(api_url1, headers=headers2, verify=False)
#print(response1.text)

#format the json
#json_object = json.loads(response1.text)
#json_formatted_str = json.dumps(json_object, indent=2)
#print the json 
#print(json_formatted_str)

#response = requests.get(api_url, verify=False)
#print(response.text)

##load the resoult of the get into json 

#format the json
#json_formatted_str = json.dumps(json_object, indent=2)
#print the json 
#print(json_formatted_str)

#json_test= response.json()

d#print(json_test["sessionid"])
