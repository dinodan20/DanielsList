from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),

]

