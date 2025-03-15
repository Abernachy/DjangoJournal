from django.contrib import admin
from django.utils.text import slugify
from .models import Journal

# Register your models here.
# class JournalAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ['journal_title']}

admin.site.register(Journal)