from django.contrib import admin
from .models import PDF
from django.utils.html import format_html


class PDFAdmin(admin.ModelAdmin):

    def thumb_f(self, obj):
        return format_html('<img src="{}" width="auto" height="100px" /> '.format(obj.thumb.url))

    thumb_f.short_description = 'thumb'

    list_display = ['name', 'thumb_f', 'pdf']


admin.site.register(PDF, PDFAdmin)
