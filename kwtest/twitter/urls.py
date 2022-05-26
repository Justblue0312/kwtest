from django.urls import path
from . import views

urlpatterns = [
    path('twitter/', views.getVietNamTwitterTrend, name='twitter'),
]
