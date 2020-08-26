from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    #username = models.CharField(max_length=50)
    #password = models.CharField(widget=forms.PasswordInput)
    displayname = models.CharField(max_length=25)
    #homepage = models.URLField(null=True)
    #age = models.IntegerField(null=True)

    def __str__(self):
        return self.username


