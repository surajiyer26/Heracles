from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main-index'),
    path('home/', views.home, name='main-home'),
]
