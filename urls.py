
from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_view),
]
