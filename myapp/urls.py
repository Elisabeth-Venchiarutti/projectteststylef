# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:00:44 2024

@author: elisa
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('image/<int:image_num>/<int:row>/', views.image, name='image'),
    path('thank_you/', views.thank_you, name='thank_you'),
]

