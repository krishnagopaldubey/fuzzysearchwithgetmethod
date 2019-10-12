from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',views.search),

]

