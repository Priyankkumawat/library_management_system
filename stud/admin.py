from django.contrib import admin
from .models import issuebook, book
from datetime import datetime
from datetime import timedelta

class issueAdmin(admin.ModelAdmin):
    list_display=[]
    # iss=issuebook.objects.all()
    # n=len(iss)
    # for i in n:
    #     if issuebook.i.test != 1:
    list_display=["name","mobile","enrollment","book","Number_of_days","isreturn"]
    list_per_page=10
    search_fields=["enrollment","book"]
    # form=Issueform
    # list_filter=[]
    list_filter=["isreturn"]

class bookAdmin(admin.ModelAdmin):
    list_display=["book_name","author_name","quantity","number"]
    list_per_page=10
    search_fields=["book_name","number"]
    list_filter=["table_num","sub_num"]

admin.site.register(issuebook, issueAdmin)
admin.site.register(book,bookAdmin)