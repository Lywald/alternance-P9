from django.urls import path
from . import views

urlpatterns = [
    # Define reviews app URLs here
    path('feed/', views.FeedView.as_view(), name='feed'),
] 