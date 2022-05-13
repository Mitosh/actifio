import requests
import json



# a function to get the sesion ID form ActifioSky Api
def get_session_id():
    api_url = "https://10.30.10.3/actifio/session"
    headers1 =  {"Authorization" : "Basic YWRtaW46T3JhbmdlMTIzIQ=="}
    response = requests.post(api_url, headers=headers1, verify=False)
    json_test= response.json()
    return json_test["session_id"]



#call the function to get seesion id and save it in sessionid variable
sessionid = get_session_id()
#print the session id
print(sessionid)



def get_application():
    api_url ="https://10.30.10.3/actifio/application?sort=appname%3Aasc&filter=hostname%3A%3D%7Cmyhost&limit=50&offset=0"
    headers = {"Authorization" : "actifio b35bcc57-1245-4feb-85fe-b3b6991dc905" }
    response = requests.get(api_url, headers=headers, verify=False)
    get_test= response.json()
    return get_test

get_apl = get_application()
print(get_apl)