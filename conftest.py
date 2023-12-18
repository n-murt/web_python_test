import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as f:
    test_data = yaml.safe_load(f)
    browser = test_data['browser']


@pytest.fixture(scope='session')
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def pass_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def btn_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def create_btn_xpath():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def find_title_xpath():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def find_desc_xpath():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def find_cont_xpath():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def add_xpath():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""


@pytest.fixture()
def title_xpath():
    return """//*[@id="app"]/main/div/div[1]/h1"""


@pytest.fixture()
def result_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""
