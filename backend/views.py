from django.shortcuts import render, redirect
from .forms import PrivateLessonForm, VolunteerForm, EventSignupForm, GroupLessonForm
from .forms import CodeForm
import csv
from .models import PrivateLesson, Volunteer, EventSignup, GroupLesson
from django.http import HttpResponse
    
def home(request):
    return render(request, 'index.html')

def private_lessons(request):
    if request.method == 'POST':
        form = PrivateLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('private_lessons_success')
        else:
            print(form.errors)  
    else:
        form = PrivateLessonForm()

    return render(request, 'private_lessons_form.html', {'form': form})
def group_lessons(request):
    if request.method == 'POST':
        form = GroupLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_lessons_success')
        else:
            print(form.errors) 
    else:
        form = GroupLessonForm()

    return render(request, 'group_lessons_form.html', {'form': form})
def private_lessons_success(request):
    return render(request, 'private_lessons_success.html')

def volunteer_request(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('volunteer_success')
        else:
            print(form.errors)
    else:
        form = VolunteerForm()
        
    return render(request, 'volunteer_form.html', {'form': form})

def event_signup(request):
    if request.method == 'POST':
        form = EventSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_signup_success')
        else:
            print(form.errors)
    else:
        form = EventSignupForm()
        
    return render(request, 'event_signup_form.html', {'form': form})


def event_signup_success(request):
    return render(request, 'event_signup_success.html')

def volunteer_success(request):
    return render(request, 'volunteer_success.html')
def gallery(request):
    return render(request, 'gallery.html')
def code_verification(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            result = "Code is valid" if code == "ansh_is_a_monkey" else "Code is invalid"
            return render(request, 'verification_result.html', {'result': result})
    else:
        form = CodeForm()
    return render(request, 'code_verification.html', {'form': form})
def export_data_to_csv(request, data_type):
    if data_type == 'private_lessons':
        data = PrivateLesson.objects.all()
        filename = 'private_lessons.csv'
    elif data_type == 'volunteers':
        data = Volunteer.objects.all()
        filename = 'volunteers.csv'
    elif data_type == 'event_signups':
        data = EventSignup.objects.all()
        filename = 'event_signups.csv'
    elif data_type == 'group_lessons':  
        data = GroupLesson.objects.all()
        filename = 'group_lessons.csv'
    else:
        return HttpResponse('Invalid data type', status=400)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in data.model._meta.fields]) 

    for item in data:
        writer.writerow([getattr(item, field.name) for field in data.model._meta.fields])

    return response

def group_lessons_success(request):
    return render(request, 'group_lessons_success.html')
