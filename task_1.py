from zeep import Client, Settings
import yaml

# settings = Settings(strict=False)

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def check_text(word):
    url = data["url"]
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    return client.service.checkText(word)[0]['s']
