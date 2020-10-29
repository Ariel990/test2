from django.contrib import admin
# Register your models here.
from userapp.models import BookInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']

admin.site.register(BookInfo, BookInfoAdmin)