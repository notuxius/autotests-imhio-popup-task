import time
from random import randint

import pytest
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


# Methods that are used in web tests:
def _sleep_time():
    # Fadein/out time from the popup code
    return time.sleep(0.3)


def _if_popup_shown_wait_find_button(driver, button):
    if driver.find_element_by_class_name("NPS__content"):
        _sleep_time()
        return button


def _click_button_input_feedback_click_send_wait(driver, popup_button):
    popup_button.click()
    feedback_area = driver.find_element_by_class_name("NPS__feedback-textarea")
    feedback_area.click()
    # Random number possibly will be used for future database auto tests for finding the right fields
    feedback_area.send_keys("Testing WebDriver {}".format(randint(0, 999999999999999999)))
    send_button = driver.find_element_by_class_name("NPS__feedback-send")
    send_button.click()
    _sleep_time()


def _click_button_wait(driver, popup_button):
    popup_button.click()
    _sleep_time()


def _button_should_not_be_clickable(popup_button):
    with pytest.raises(StaleElementReferenceException) as e:
        popup_button.click()


def _feedback_should_not_be_visible(driver):
    with pytest.raises(NoSuchElementException) as e:
        driver.find_element_by_class_name("NPS__input_feedback-textarea")


# Web desktop tests:
def test_click_button_0_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n0"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_1_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n1"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_2_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n2"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_3_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n3"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_4_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n4"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_5_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n5"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_6_input_feedback_desktop(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n6"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_7_desktop(driver, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n7"))
    _click_button_wait(driver, popup_button)
    _feedback_should_not_be_visible(driver)


def test_click_button_8_desktop(driver, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n8"))
    _click_button_wait(driver, popup_button)
    _feedback_should_not_be_visible(driver)


def test_click_button_9_desktop(driver, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n9"))
    _click_button_wait(driver, popup_button)
    _feedback_should_not_be_visible(driver)


def test_click_button_10_desktop(driver, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver,
                                                    driver.find_element_by_css_selector(".NPS__button-container.n10"))
    _click_button_wait(driver, popup_button)
    _feedback_should_not_be_visible(driver)


# Web mobile tests:
def test_click_button_5_input_feedback_mobile(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver, driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[5]/div[6]/div"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_6_input_feedback_mobile(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver, driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[5]/div[5]/div"))
    _click_button_input_feedback_click_send_wait(driver, popup_button)
    _button_should_not_be_clickable(popup_button)


def test_click_button_7_mobile(driver, chrome_options, connect_to_url_port):
    popup_button = _if_popup_shown_wait_find_button(driver, driver.find_element_by_xpath(
        "/html/body/div[2]/div[1]/div[5]/div[4]/div"))
    _click_button_wait(driver, popup_button)
    _feedback_should_not_be_visible(driver)
