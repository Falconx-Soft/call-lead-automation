from django.db import models

# Create your models here.

class access_token(models.Model):

    token            = models.CharField(max_length = 300)

    def __str__(self):
        return self.token
