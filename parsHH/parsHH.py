import requests

def get_all_dict(url, params):
    headers = params["headers"]
    body = params['body']
    if params["method"] == "GET":
        return create_dict(requests.get(url, headers=headers))
    if params["method"] == 'POST':
        return create_dict(requests.post(url, headers=headers, data=body))
def create_dict(diction):
    professions = diction  #get_all_dict("https://api.hh.ru/specializations", {
    #     "headers": {
    #         "User-Agent": "MyApp/1.0"
    #     },
    #     "body": None,
    #     "method": "GET"
    # })
    id_list = []
    name_list = []
    for i in professions.json():
        for id in i['specializations']:
            id_list.append(id["id"])
            name_list.append(id["name"])
    diction = dict(zip(id_list, name_list))
    return diction

dict_proffession = create_dict(diction={})
print(dict_proffession)
