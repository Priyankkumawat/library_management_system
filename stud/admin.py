from django.contrib import admin
from .models import IssueBook, Studbook

class issueAdmin(admin.ModelAdmin):
    list_display=[]
    list_display=["name","mobile","enrollment","book","Number_of_days","isreturn"]
    list_per_page=10
    search_fields=["enrollment","book"]
    list_filter=["isreturn"]

class bookAdmin(admin.ModelAdmin):
    list_display=["book_name","author","quantity","number"]
    list_per_page=10
    search_fields=["book_name","number"]
    list_filter=["table_number","subject_num"]

admin.site.register(IssueBook, issueAdmin)
admin.site.register(Studbook,bookAdmin)