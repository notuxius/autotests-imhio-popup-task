import re

import pytest


@pytest.fixture
def url_port_endp():
    url_port_valid_endp = "http://192.168.99.100:58001/nps"
    url_port_inval_endp = "http://192.168.99.100:58001/nnn"
    url_port_empty_endp = "http://192.168.99.100:58001/"
    return [url_port_valid_endp, url_port_inval_endp, url_port_empty_endp]


@pytest.fixture()
def chrome_options(request, chrome_options):
    # Disable the W3C when initializing the Chrome driver
    chrome_options.add_experimental_option("w3c", False)
    chrome_options.add_argument("--start-maximized")

    # Workaround, depending on test function name with or without "mobile" in it Chrome will run with different options
    # don't know how to use different chrome_options fixture for different tests
    for key in dict(request.keywords):
        if re.search("mobile", key):
            device_name = {"deviceName": "iPhone X"}
            chrome_options.add_experimental_option("mobileEmulation", device_name)
            # device_metrics = {"deviceMetrics": {"width": 760}}
            # chrome_options.add_experimental_option("mobileEmulation", device_metrics)
    return chrome_options


@pytest.fixture
def connect_to_url_port(driver, url_port_endp):
    # url_port_endp[2] - use just URL without endpoint
    driver.get(url_port_endp[2])
    return connect_to_url_port
