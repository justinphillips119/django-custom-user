from django.contrib import admin
from custom_user_app.models import CustomUser
#from django.contrib.auth.admin import UserAdmin



admin.site.register(CustomUser)
