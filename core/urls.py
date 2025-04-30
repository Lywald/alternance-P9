from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'), # Map root URL to HomeView
    path('signup/', views.SignupView.as_view(), name='signup'), # Add signup URL
] 