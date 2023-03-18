import time

from selenium.webdriver.common.by import By

from outreach.api.constant import CSS_SELECTOR
from outreach.api.utils import wait, random_wait
from outreach.models import LinkedinCookies, LinkedinOutreach


def linkedin_login(driver, username):
    driver.get("https://www.linkedin.com/home")
    wait(100)
    save_cookies(driver, username)


def save_cookies(driver, username):
    cookies = driver.get_cookies()
    cookies_instance = LinkedinCookies.objects.filter(username=username).first()

    if cookies_instance:
        cookies_instance.is_deleted = True
        cookies_instance.save()

    LinkedinCookies.objects.create(username=username, cookies=cookies)


def get_cookies(username):
    cookies_instance = LinkedinCookies.objects.filter(username=username).first()
    if cookies_instance:
        return cookies_instance.cookies
    else:
        return None


def linkedin_outreach(driver, linkedin_url_list, message, linkedin_url_tab_name):
    try:
        for each_url in linkedin_url_list:
            name = ''
            linkedin = each_url[linkedin_url_tab_name]

            if linkedin != '' and LinkedinOutreach.objects.filter(linkedin_url=linkedin).count() == 0:
                if connect_request_sent(driver, message, linkedin):
                    LinkedinOutreach.objects.create(name=name, linkedin_url=linkedin)

            wait(1)

    except Exception as ex:
        print(ex)


def connect_request_sent(driver, message, prospect_linkedin):
    is_sent = False
    url = prospect_linkedin

    if check_user(driver, message, url):
        is_sent = True

    return is_sent


def check_user(driver, message, url):
    request_sent = False
    try:
        driver.get(url)
        first_name = driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR['profile_heading']).text.split(" ")[0]

        message = message.format(first_name)
        random_wait(1, 3)
        buttons = driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR['buttons']).text.splitlines()

        random_wait(2, 4)

        if buttons[0].lower() == "message" or buttons[0].lower() == "follow":

            request_sent = more_button(driver, request_sent, message)

        elif buttons[0].lower() == "pending":
            request_sent = True
        else:
            button_list = driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR['buttons'])
            button_list.find_element(By.CLASS_NAME, 'artdeco-button').click()
            random_wait(2, 5)
            request_sent = add_note(driver, request_sent, message)

        return request_sent
    except Exception as ex:

        return request_sent


def add_note(driver, request_sent, message):
    try:
        driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR['add_note_button']).click()
        note_area = driver.find_element(By.ID, 'custom-message')

        random_wait(2, 4)

        note_area.send_keys(message)
        random_wait(1, 3)

        # send button
        driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR['send_button']).click()
        request_sent = True

        return request_sent
    except Exception as ex:
        return request_sent


def more_button(driver, request_sent, message):
    try:
        driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR['more_button'])[1].click()
        wait(5)

        i = 1
        for item in driver.find_elements(By.CSS_SELECTOR, CSS_SELECTOR['more_button_dropdown']):
            if item.text == "Connect":
                item.click()

                random_wait(2, 5)

            elif item.text.lower() == "pending":
                request_sent = True
                return request_sent

            elif item.text.lower() == "remove connection":
                return True
            i += 1

        request_sent = add_note(driver, request_sent, message)
        return request_sent

    except Exception as ex:

        return request_sent


def get_recent_accept_request_list(driver):
    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
    time.sleep(5)
    connection_list = driver.find_element(By.CLASS_NAME, 'scaffold-finite-scroll__content')
    details_card = connection_list.find_elements(By.CLASS_NAME, 'mn-connection-card')
    person_list = []
    for each_person in details_card:
        name_div = each_person.find_element(By.CLASS_NAME, 'mn-connection-card__name')
        name = name_div.text
        linkedin_div = each_person.find_element(By.CLASS_NAME, 'mn-connection-card__picture')
        linkedin = linkedin_div.get_attribute('href')
        position_div = each_person.find_element(By.CLASS_NAME, 'mn-connection-card__occupation')
        position = position_div.text
        accepted_time_div = each_person.find_element(By.CLASS_NAME, 'time-badge')
        accepted_time = accepted_time_div.text
        temp_list = accepted_time.split(' ')
        # if 'seconds' in temp_list or 'hours' in temp_list or 'minutes' in temp_list:
        person_list.append(
            {'name': name, 'linkedin': linkedin, 'position': position, 'acceptance_time': accepted_time}
        )
    return person_list
