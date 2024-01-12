from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsPageView.as_view(), name='aboutus'),
    path('roadmap/', views.RoadMapPageView.as_view(), name='roadmap'),
    path('activity/', views.ActivityPageView.as_view(), name='activity'),


]