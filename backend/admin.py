from django.contrib import admin
from .models import PrivateLesson, Volunteer

@admin.register(PrivateLesson)
class PrivateLessonAdmin(admin.ModelAdmin):
    list_display = ('childs_name', 'contact_phone_number', 'contact_email', 'preferred_coach')
    list_filter = ('preferred_coach',)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_phone_number', 'contact_email', 'skills')