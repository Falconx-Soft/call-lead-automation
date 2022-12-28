from django.db import models

from ckeditor.fields import RichTextField

class terms_and_condition(models.Model):
    terms_and_condition                                = RichTextField()


class privacy_policy(models.Model):
    terms_and_privacy                                = RichTextField()