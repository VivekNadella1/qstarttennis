from django import forms
from .models import EventSignup, PrivateLesson, Volunteer, GroupLesson

class PrivateLessonForm(forms.ModelForm):
    class Meta:
        model = PrivateLesson
        fields = ['childs_name', 'contact_phone_number', 'contact_email', 'preferred_coach']

class GroupLessonForm(forms.ModelForm):
    class Meta:
        model = PrivateLesson
        fields = ['childs_name', 'contact_phone_number', 'contact_email']


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['full_name', 'contact_phone_number', 'contact_email', 'skills']

class EventSignupForm(forms.ModelForm):
    class Meta:
        model = EventSignup
        fields = ['full_name', 'contact_phone_number', 'contact_email', 'participating_in_tournament']
class CodeForm(forms.Form):
    code = forms.CharField(label='Enter the Code', max_length=100)