
from django.urls import path
from . import views
urlpatterns = [
    path('', views.auth_login, name='login'),
    path('main/', views.main_view ,name='main_view'),
    path('lgout', views.lout, name='LogOut')
]