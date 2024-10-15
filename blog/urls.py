from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('healthcare/', views.healthcare_page, name='healthcare_page'),
    path('finance/', views.finance_page, name='finance_page'),
    path('insurance/', views.insurance_page, name='insurance_page'),
]