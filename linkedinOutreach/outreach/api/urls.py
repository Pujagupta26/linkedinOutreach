from django.urls import path

from outreach.api.views import LinkedinOutreachUsingGoogleSheet, LinkedinLogin

urlpatterns = [
    path("linkedin/googleSheet", LinkedinOutreachUsingGoogleSheet.as_view(), name="outreach using google sheet"),
    path("linkedin/login", LinkedinLogin.as_view(), name="linkedin login"),

]
