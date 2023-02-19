import requests

def fetch(url, params):
    headers = params["headers"]
    body = params['body']
    if params["method"] == "GET":
        return requests.get(url, headers=headers)
    if params["method"] == 'POST':
        return requests.post(url, headers=headers, data=body)

professions = fetch("https://api.hh.ru/specializations", {
  "headers": {
    "User-Agent": "MyApp/1.0"
  },
  "body": None,
  "method": "GET"
})

id_list = []
name_list = []

for i in professions.json():
    for id in i['specializations']:
        id_list.append(id["id"])
        name_list.append(id["name"])

diction = dict(zip(id_list, name_list))
print(diction)