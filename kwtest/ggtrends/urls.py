from django.urls import path
from . import views

urlpatterns = [
    path('trends_home/', views.trends_home, name='trends_home'),
    path('ggtrends/', views.trend_index, name='trend_index'),
    path('search/', views.search, name='search'),
]
