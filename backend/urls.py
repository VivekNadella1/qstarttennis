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
    path('code-verification/', views.code_verification, name='code-verification'),

    # Add export URLs
    path('export/private_lessons/', views.export_data_to_csv, {'data_type': 'private_lessons'}, name='export-private-lessons'),
    path('export/volunteers/', views.export_data_to_csv, {'data_type': 'volunteers'}, name='export-volunteers'),
    path('export/event_signups/', views.export_data_to_csv, {'data_type': 'event_signups'}, name='export-event-signups'),
    
    # Add group form URLs
    path('group_lessons/', views.group_lessons, name='group_lessons'),
    path('group_lessons_success/', views.group_lessons_success, name='group_lessons_success'),
    path('export/group_lessons/', views.export_data_to_csv, {'data_type': 'group_lessons'}, name='export-group-lessons'),
]