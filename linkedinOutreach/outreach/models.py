from django.db import models

from utils.models import TimeStampedModel


# Create your models here.
class LinkedinCookies(TimeStampedModel):
    username = models.CharField(max_length=255)
    cookies = models.TextField()


class LinkedinOutreach(TimeStampedModel):
    name = models.CharField(max_length=255)
    linkedin_url = models.TextField()
