from django.contrib import admin
from .models import Page, News

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'text')

admin.site.register(Page, PageAdmin)
admin.site.register(News, NewsAdmin)