import random
import time

from selenium import webdriver

from outreach.api.constant import BINARY_LOCATION, CHROMEDRIVER_LOCATION, cookies_expired_url_list


def wait(t):
    time.sleep(t)


def random_wait(a, b):
    t = random.randint(a, b)
    wait(t)


def chrome_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = BINARY_LOCATION

    web_driver = webdriver.Chrome(executable_path=CHROMEDRIVER_LOCATION, chrome_options=options)
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    return web_driver


def add_cookies_in_driver(driver, cookies):
    driver.get("https://www.linkedin.com")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://www.linkedin.com")
    return driver


def verify_cookies(url):
    try:
        question_mark_index = url.index("?")
        url_sub = url[:question_mark_index]
    except:
        url_sub = url

    if url_sub in cookies_expired_url_list:
        return False
    else:
        return True

