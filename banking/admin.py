from django.contrib import admin
from .models import Credit, Transaction

# Register your models here.
admin.site.register(Credit)
admin.site.register(Transaction)