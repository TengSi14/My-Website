from django.urls import path
from app_site import views

app_name = 'app_site'
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills'),
    path('career', views.career, name='career'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
    ]