from django.contrib import admin
from . import models

class IdeaAdmin(admin.ModelAdmin):
    list_display = ['title', 'pitch', 'votes', 'id', 'creation_date']


admin.site.register(models.Idea, IdeaAdmin)