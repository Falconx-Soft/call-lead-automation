from django.db import models

# Create your models here.
class webhook_data(models.Model):
    data                        = models.JSONField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = ("Webhook data")
        verbose_name_plural = ("Webhook data")  
