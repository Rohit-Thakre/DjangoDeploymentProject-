from django.urls import path
from sub_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]