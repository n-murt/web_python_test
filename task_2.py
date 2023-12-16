import pytest
import requests
import yaml

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
    return res_get.json()['data'][0]['id']
