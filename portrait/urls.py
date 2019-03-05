from django.urls import path
from . import views

app_name = 'mobi'
urlpatterns = [
    path('', views.index, name='index'),
]
