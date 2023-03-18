from oauth2client.service_account import ServiceAccountCredentials
CHROMEDRIVER_LOCATION = "C:/Users/gkhom/Desktop/chrome_driver/chromedriver"
BINARY_LOCATION = "C:/Program Files/Google/Chrome/Application/chrome.exe"



CSS_SELECTOR = {
#ember31 > div.ph5.pb5 > div.pv-top-card-v2-ctas.display-flex.pt3 > div
    "buttons": "div.pv-top-card-v2-ctas",
#ember29 > div.ph5.pb5 > div.pv-top-card-v2-ctas
#ember29 > div.ph5.pb5 > div.pv-top-card-v2-ctas
#ember29 > div.ph5.pb5 > div.pv-top-card-v2-ctas > div
    "employees": "span.link-without-visited-state.t-bold.t-black--light",
    "profile_detail": "div.entity-result__content.entity-result__divider.pt3.pb3.t-12.t-black--light",
    "result": "div.pb2.t-black--light.t-14",
    "profile_heading": "h1.text-heading-xlarge.inline.t-24.v-align-middle.break-words",
    "desc": "div.text-body-medium.break-words",
    "emp_button": "div.display-flex.mt2.mb1",
    "company_detail": "div.block.mt2",
    "company_website": "a.ember-view.org-top-card-primary-actions__action",
    # driver.find_elements_by_css_selector('div.artdeco-dropdown.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-left.ember-view')
    # 'more_button': 'div.artdeco-dropdown.artdeco-dropdown--placement-bottom.artdeco-dropdown--justification-right.ember-view',
    'more_button': 'button.artdeco-dropdown__trigger.artdeco-dropdown__trigger--placement-bottom.ember-view.pvs-profile-actions__action.artdeco-button.artdeco-button--secondary.artdeco-button--muted.artdeco-button--2',

    'more_button_dropdown': 'span.display-flex.t-normal.flex-1',
    'connect_inside_button': 'button.mr2.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view',
    'add_note_button': 'button.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1',
    # 'more_button' :'button.artdeco-button.artdeco-button--muted.artdeco-button--2.artdeco-button--secondary.ember-view.mr1',
    #             textarea.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3
    'note_area': 'textarea.ember-text-area.ember-view.connect-button-send-invite__custom-message.mb3',

    'send_button': 'button.ml1.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view',
    'connct_button': 'button.artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view.pvs-profile-actions__action',
    'connect_button': '#ember73',
}

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("utils/credentials/cred.json", scope)

sheet_name = 'Outreach-Job'
tab_name = 'Sheet1'

cookies = [{'domain': '.linkedin.com', 'expiry': 1686676713, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1.1.111048311.1678900714'}, {'domain': '.linkedin.com', 'expiry': 1694452707, 'httpOnly': False, 'name': 'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '-637568504%7CMCIDTS%7C19432%7CMCMID%7C81179072189630848763432821661116741580%7CMCAAMLH-1679505507%7C12%7CMCAAMB-1679505507%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1678907907s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C344773678'}, {'domain': '.linkedin.com', 'expiry': 1678965782, 'httpOnly': False, 'name': 'lidc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"b=VB90:s=V:r=V:a=V:p=V:g=3327:u=445:x=1:i=1678900706:t=1678965782:v=2:sig=AQEjmYgvpbkBdL8oB6_4jp7xVnfl_G1i"'}, {'domain': '.linkedin.com', 'expiry': 1681492706, 'httpOnly': False, 'name': 'lms_ads', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEzHOxmZOVaGQAAAYbmR7qWRNZoURz3pwWqVmATGUlbGa5UclxYd6qTzJ-y6rT4qjhbyIpeylWHk9fMMbHXeDhy8mlTk7Wl'}, {'domain': '.linkedin.com', 'expiry': 1681492705, 'httpOnly': False, 'name': 'AnalyticsSyncHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQLzFjv1VN6EmgAAAYbmR7jwIJ-hX9-qngBqarGBFNKiZ6JDv_RZFiJNaOVnpgAeBV4DLDUk3Osab9JIuX09Lg'}, {'domain': '.linkedin.com', 'expiry': 1681492705, 'httpOnly': False, 'name': 'UserMatchHistory', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQIJGQSpqT0TqAAAAYbmR7jwkNS5POQkXdSWvevecVRTOwKVE_0KqQzzKWHa0rugAGT3GIhcCpS0MlILWiaaeE0MS1JJnBCDzEjCG5U3tZPbOqlbaLezAKF13IpWgW5NF8tsye5dM-p8oNP0ai3nkqRimF0R0YrHM4OlP-PTXdHqdxgA17UDrj27DNSYefgcqBS6c-d2wXOYnrtHuPce5vy2vA4h9eemppQ3G9y4M5xanlilcbhUKX-XbUdrFzs6qPpB8mPJQII7g5h4JzVX_M1gTV0iBiI4UBaMBaI'}, {'domain': '.linkedin.com', 'expiry': 1686676706, 'httpOnly': False, 'name': 'li_sugr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '601990c1-7b1a-4c80-81c5-3166cc28c2be'}, {'domain': '.linkedin.com', 'expiry': 1686676705, 'httpOnly': False, 'name': '_guid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2877946d-2662-4f3b-9257-c6096345d910'}, {'domain': '.www.linkedin.com', 'expiry': 1710436706, 'httpOnly': True, 'name': 'bscookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=1&20230315171724def86128-4590-476f-8a62-e05225d80e3bAQFP021C4llwRt_hgtPkPROXjsBmNjC-"'}, {'domain': '.linkedin.com', 'expiry': 1686676699, 'httpOnly': False, 'name': 'liap', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'true'}, {'domain': '.linkedin.com', 'expiry': 1710436706, 'httpOnly': False, 'name': 'bcookie', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"v=2&31e5a9dd-95e2-438c-8ea8-67f616da4202"'}, {'domain': '.www.linkedin.com', 'expiry': 1694452703, 'httpOnly': False, 'name': 'li_theme', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'light'}, {'domain': '.www.linkedin.com', 'expiry': 1710436699, 'httpOnly': True, 'name': 'li_at', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEDATAFB5YFdVs3AAABhuZHoCoAAAGHClQkKk0AmFxNTt8VK9XniFiFfO9_7pUXtaENDuw2RYDq9W9DoYJiIKTIOiP1T5OHEYdP5UdTo25tqwkRb9lybG0O9Aj9kikFBkNZ0ZLWW9nVgOMXlpODj3lu'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'lang', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v=2&lang=en-us'}, {'domain': '.linkedin.com', 'expiry': 1681492706, 'httpOnly': False, 'name': 'lms_analytics', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AQEzHOxmZOVaGQAAAYbmR7qWRNZoURz3pwWqVmATGUlbGa5UclxYd6qTzJ-y6rT4qjhbyIpeylWHk9fMMbHXeDhy8mlTk7Wl'}, {'domain': '.www.linkedin.com', 'expiry': 1694452703, 'httpOnly': False, 'name': 'li_theme_set', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'app'}, {'domain': '.www.linkedin.com', 'expiry': 1713460645, 'httpOnly': False, 'name': 'G_ENABLED_IDPS', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'google'}, {'domain': '.www.linkedin.com', 'expiry': 1680110303, 'httpOnly': False, 'name': 'timezone', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'Asia/Calcutta'}, {'domain': '.www.linkedin.com', 'expiry': 1686676699, 'httpOnly': False, 'name': 'JSESSIONID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '"ajax:7551798672465757496"'}, {'domain': '.linkedin.com', 'expiry': 1681492714, 'httpOnly': False, 'name': 'aam_uuid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '80996432803589830473417381234036425735'}, {'domain': '.linkedin.com', 'httpOnly': False, 'name': 'AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1'}]
# message = "Hi, {} \n" \
#           "Happy to connect with you.\n" \
#           "I’m good at backend development and have experience of 1 years.\n" \
#           "Looking forward to discuss with you if you’ve any requirements related to backend\n" \
#           "Please do let me know\n" \
#           "Thanks and regards,\n" \
#           "Gourav"

message = "Hi, {} \n" \
          "Thanks for accepting my request.\n" \
          "I am a final year CSE student, looking for an opportunity in this industry.\n" \
          "It would be great to know if I'm a fit for any of your openings.\n"\
          "I'm available to discuss further on my experience and skills.\n" \
          "Thanks"


cookies_expired_url_list = [
    "https://www.linkedin.com/hp",
    "https://www.linkedin.com/authwall",
]