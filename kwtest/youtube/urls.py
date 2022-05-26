from django.urls import path
from . import views

urlpatterns = [
    path('youtube/', views.getTopYtVideo, name='youtube'),
]
