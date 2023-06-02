from django.urls import path 
from .views import index, password, about

app_name = 'generator'

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('password', password, name='password')
]
