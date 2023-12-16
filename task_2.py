import pytest
import requests
import yaml
import json

with open('config.yaml') as f:
    data = yaml.safe_load(f)

url = data["url2"]
login = data["login"]
password = data["password"]
url_post = data["url_post"]


def get_id():
    result = requests.post(url=url, data={"username": login, "password": password})
    token = result.json()["token"]
    res_get = requests.get(url=url_post, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    result_get = res_get.json()['data']

    res_id_list = [item['id'] for item in result_get]

    return res_id_list


#get_id()
