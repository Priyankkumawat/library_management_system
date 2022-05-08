import imp
from operator import imod
from django import urls
from django.urls import path
from . import views
from django.contrib import admin
# from django.contrib import admin

admin.site.site_header="Login to Library Management system"
admin.site.site_title="Library Management system"
admin.site.index_title="Welcome to Admin Portel"

urlpatterns = [
    path('',views.index, name="index"),
    path('issue',views.issue,name="issue"),
    path('search',views.search,name="search"),
    # path('delete/<event_id>',views.delete, name="delete")
]
