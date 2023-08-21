from django.shortcuts import render, redirect
from .forms import PrivateLessonForm, VolunteerForm, EventSignupForm

def home(request):
    return render(request, 'index.html')

def private_lessons(request):
    if request.method == 'POST':
        form = PrivateLessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('private_lessons_success')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = PrivateLessonForm()

    return render(request, 'private_lessons_form.html', {'form': form})
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