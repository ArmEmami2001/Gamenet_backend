from django.contrib import admin

from . import models

admin.site.register(models.Subs)
admin.site.register(models.Worker)
admin.site.register(models.Customer)