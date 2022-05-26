from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.get_about, name='about'),
    path('contact/', views.get_contact, name='contact'),

    path('sucess/', views.successView, name='sucess'),

    path('yake/', views.handle_yake_alg, name='yake'),
    path('rake/', views.handle_rake_alg, name='rake'),
]
