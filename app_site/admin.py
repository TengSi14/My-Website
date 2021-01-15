from django.contrib import admin
from .models import Messages
# Register your models here.

#para iconnect natin yung models sa admin panel ng django.
admin.site.register(Messages)