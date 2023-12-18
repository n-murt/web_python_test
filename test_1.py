import pytest

from testpage import OperationHelper
import logging
import time

import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test 1 Старт")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    time.sleep(3)
    assert testpage.get_error_text() == "401", "Test_1 FAIL"


def test_step2(browser):
    logging.info("Test2 Старт")
    testpage = OperationHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(data['login'])
    testpage.enter_pass(data['password'])
    testpage.click_login_button()
    time.sleep(2)
    assert testpage.get_profile_text() == f"Hello, {data['login']}", "Test_2 FAIL"


def test_step3(browser):
    logging.info("Test3 Старт")
    testpage = OperationHelper(browser)
    testpage.click_to_do_new_post()
    testpage.enter_title("title test")
    testpage.enter_description("description test")
    testpage.enter_content("content test")
    testpage.click_save_post_button()
    time.sleep(5)
    assert testpage.get_title_text() == "title test", "Test_3 FAIL"


def test_step4(browser):
    logging.info("Test4 Старт")
    testpage = OperationHelper(browser)
    testpage.click_contact_button()
    testpage.enter_name("test name")
    testpage.enter_email("test@example.com")
    testpage.enter_contact_content("test contact")
    testpage.contact_us_save_button()
    time.sleep(3)
    assert testpage.get_alert_text() == "Form successfully submitted", "Test_4 FAIL"
