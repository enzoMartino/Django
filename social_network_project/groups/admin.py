from django.contrib import admin
from . import models

# Register your models here.

class GroupAdmin(admin.ModelAdmin):

    fields = ['description', 'name', 'slug',]

    search_fields = ['name']

    list_filter = ['members']

    list_display = ['id', 'name', 'description', 'slug',]

    list_display_links = ['id']

    list_editable = ['name',]



class GroupMemberInline(admin.TabularInline):

    model = models.GroupMember

admin.site.register(models.Group, GroupAdmin)

admin.site.register(models.GroupMember)
