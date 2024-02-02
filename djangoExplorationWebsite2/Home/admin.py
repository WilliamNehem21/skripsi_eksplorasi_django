from django.contrib import admin

# Register your models here.
from .models import Home

class HomeAdmin(admin.ModelAdmin):
    readonly_fields = ['slug',]

admin.site.register(Home, HomeAdmin)