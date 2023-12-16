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

title = 'title test'
description = 'description test'
content = 'content test'


def create_post():
    result = requests.post(url=url, data={"username": login, "password": password})
    token = result.json()["token"]

    data_post = {
        "title": title,
        "description": description,
        "content": content
    }
    res_post = requests.post(url=url_post, headers={"X-Auth-Token": token}, data=data_post)
    print(res_post.json())
    return res_post.json()


#create_post(title, description, content)
