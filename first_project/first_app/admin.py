from django.contrib import admin
from first_app import models

# Register your models here.

admin.site.register(models.AccessRecord)
admin.site.register(models.Topic)
admin.site.register(models.WebPage)
admin.site.register(models.UserProfileInfo)
admin.site.register(models.School)
admin.site.register(models.Student)