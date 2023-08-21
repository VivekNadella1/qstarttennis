from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('private-lessons/', views.private_lessons, name='private_lessons'),
    path('private-lessons/success/', views.private_lessons_success, name='private_lessons_success'),
    path('volunteer/', views.volunteer_request, name='volunteer_request'),
    path('volunteer/success/', views.volunteer_success, name='volunteer_success'),
    path('gallery/', views.gallery, name='gallery'),
    path('event-signup/', views.event_signup, name='event_signup'),
    path('event-signup/success/', views.event_signup_success, name='event_signup_success'),
]