# blog/urls.py
from django.urls import path
from . import views

app_name = 'excels'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('create-excel/', views.create_excel, name='create_excel'),
    path('setting/', views.setting, name='setting'),
    path('store_excel_data/', views.store_excel_data, name='store_excel_data'),
    # Add more URL patterns here
]