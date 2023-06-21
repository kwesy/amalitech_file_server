from django.contrib import admin
from .models import Document, Tag, Category

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    readonly_fields=('num_downloads','num_emails_sent')


admin.site.register(Document,DocumentAdmin)
admin.site.register([Tag, Category])

