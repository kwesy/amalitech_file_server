from django.contrib import admin
from .models import Document, Tag, Category

# Register your models here.


admin.site.register([Document, Tag, Category])

