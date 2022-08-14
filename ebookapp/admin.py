from django.contrib import admin
from .models import Book
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):

    def thumb_f(self, obj):
        return format_html('<img src="{}" width="60" height="60" /> '.format(obj.thumb.url))

    thumb_f.short_description = 'thumb'
    list_display = ['name', 'thumb_f', 'pdf']

admin.site.register(Book, BookAdmin)

