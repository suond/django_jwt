from django.urls import re_path, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('signup', views.signup),
    path('test_token', views.test_token),
]
