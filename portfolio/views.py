from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact, Project

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='login')
def home(request):

    projects = Project.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

    return render(request, 'home.html', {'projects': projects})

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        msg = data.get("message", "").lower()

        if "hi" in msg or "hello" in msg:
            reply = "Hello! Welcome to my portfolio."

        elif "about" in msg:
            reply = "I am Suparna Duary, a Frontend and Django Developer."

        elif "who are you" in msg:
            reply = "I am Suparna Duary, Frontend Web Developer."

        elif "skills" in msg:
            reply = "My skills are HTML, CSS, JavaScript, Python, Django and Bootstrap."

        elif "projects" in msg:
            reply = "I have built Weather App, RedBus Clone, Calculator, Todo App and Portfolio Website."

        elif "contact" in msg:
            reply = "You can contact me through LinkedIn."

        elif "resume" in msg or "cv" in msg:
            reply = "You can download my CV using the Download CV button."

        elif "django" in msg:
            reply = "I use Django for backend web development."

        elif "react" in msg:
            reply = "I have worked with React.js for frontend development."

        elif "experience" in msg:
            reply = "I am a fresher developer and have built multiple projects using HTML, CSS, JavaScript and Django."

        else:
            reply = "Try asking: about, skills, projects, contact, resume."

        return JsonResponse({"reply": reply})