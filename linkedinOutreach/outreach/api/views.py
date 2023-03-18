from rest_framework import generics, status

from outreach.api import utils
from outreach.api.action import linkedin_login, get_cookies, linkedin_outreach
from outreach.api.constant import message
from outreach.api.utils import add_cookies_in_driver, verify_cookies
from utils.googleSheet_operations import read_google_sheet
from utils.restful_response import send_response


class LinkedinOutreachUsingGoogleSheet(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        username = request.GET.get("username")
        sheet_name = request.GET.get("sheetName")
        tab_name = request.GET.get("tabName")
        linkedin_url_tab_name = request.GET.get("linkedinUrlTabName")

        if not username or not sheet_name or not tab_name or not linkedin_url_tab_name:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message="parameter is required",
                ui_message="parameter is required",
            )
        driver = utils.chrome_driver()
        cookies = get_cookies(username)

        if cookies is None:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message="cookies not found",
                ui_message="cookies not found",
            )

        add_cookies_in_driver(driver, eval(cookies))
        driver.get("https://www.linkedin.com/mynetwork/invitation-manager/sent/")
        current_url = driver.current_url

        if not verify_cookies(current_url):
            driver.close()
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message="cookies expired",
                ui_message="cookies expired",
            )
        try:
            data, sheet_instance = read_google_sheet(sheet_name, tab_name)
            linkedin_outreach(driver, data, message, linkedin_url_tab_name)
        except Exception as e:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message=str(e),
                ui_message="Please share google sheet to thsi email id "
                           "stackoverflowscrapper@stackoverflowscrapper-328308.iam.gserviceaccount.com",
            )

        return send_response(
            status=status.HTTP_200_OK,
            developer_message="outreach done successfully",
            ui_message="outreach done successfully",
        )


class LinkedinLogin(generics.RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        username = request.GET.get("username")
        if not username:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message="username is required",
                ui_message="username is required",
            )
        try:
            driver = utils.chrome_driver()
            linkedin_login(driver, username)
            driver.close()
            return send_response(
                status=status.HTTP_200_OK,
                developer_message="login done successfully",
                ui_message="login done successfully",
            )
        except Exception as e:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                developer_message=str(e),
                ui_message=str(e),
            )
