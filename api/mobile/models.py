from django.db import models

# Create your models here.


class Mobile(models.Model):
    mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.mobile
