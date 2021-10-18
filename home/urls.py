from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name="gallery"),
    path('about/', views.about, name="about"),
    path('upcoming_classes/', views.upcoming_class, name="upcoming_classes"),
    path('semi/', views.semi, name="semi"),
    path('feedback/', views.feedback, name="feedback"),
    path('Bharatanatyam/', views.Bharatanatyam, name="Bharatanatyam"),
    path('prarambhik/', views.prarambhik, name="prarambhik"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('classes/', views.classes, name="classes"),
]
