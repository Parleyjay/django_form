from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('form', views.user_form, name = 'user-form'),

]
