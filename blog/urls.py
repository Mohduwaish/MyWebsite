from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header="Epsilon Admin"
admin.site.site_title="Epsilon Admin Panel"
admin.site.index_title="Welcome to Epsilon Admin Panel"

urlpatterns = [
    path('postComment', views.postComment, name='postComment'),
    path('', views.bloghome, name="bloghome"),
    path('<str:slug>', views.blogpost, name="blogpost"),
]
