from django.urls import path, re_path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<id>', views.category, name='category'), 
]