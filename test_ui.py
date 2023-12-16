import time

import yaml
from task_ui import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step1(login_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", login_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_label = site.find_element("xpath", result_xpath)
    assert err_label.text == "401"


def test_step2(login_xpath, pass_xpath, btn_xpath, create_btn_xpath, find_title_xpath, find_desc_xpath, find_cont_xpath,
               add_xpath, title_xpath):
    input1 = site.find_element("xpath", login_xpath)
    input1.clear()
    input1.send_keys("petrov999")
    input2 = site.find_element("xpath", pass_xpath)
    input2.clear()
    input2.send_keys("d6b4c8961c")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    # x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    # err_label = site.find_element("xpath", x_selector3)
    # assert err_label.text == "401"
    time.sleep(3)

    input1 = site.find_element("xpath", create_btn_xpath)
    input1.click()
    time.sleep(3)

    input1 = site.find_element("xpath", find_title_xpath)
    input1.send_keys("TEST TITLE")
    input2 = site.find_element("xpath", find_desc_xpath)
    input2.send_keys("TEST DESCRIPTION")
    input3 = site.find_element("xpath", find_cont_xpath)
    input3.send_keys("TEST CONTENT")
    time.sleep(3)

    input4 = site.find_element("xpath", add_xpath)
    input4.click()
    time.sleep(3)

    text_label = site.find_element("xpath", title_xpath)
    assert text_label.text == 'TEST TITLE'
