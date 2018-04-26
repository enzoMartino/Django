from django.contrib import admin
from . import models

# Register your models here.

class GroupAdmin(admin.ModelAdmin):

    fields = ['description', 'name', 'slug',]


class GroupMemberInline(admin.TabularInline):

    model = models.GroupMember

admin.site.register(models.Group, GroupAdmin)

admin.site.register(models.GroupMember)
