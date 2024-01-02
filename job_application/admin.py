from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email")
    search_fields = ("first_name","last_name","email")
    list_filter = ("date","occupation")
    ordering = ("-first_name",)
    readonly_fields = ('occupation',)

admin.site.register(Form, FormAdmin)


# Open terminal and run the following:
#     python manage.py runserver


# TYPE "http://127.0.0.1:8000/admin/" IN EDGE AFTER "python manage.py runserver" IN TERMINAL


# Username (leave blank to use 'jayachandran'): sanju
# Email address: sanjanaarj2003@gmail.com
# Password: sanju

