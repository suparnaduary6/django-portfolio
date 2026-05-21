from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Contact, Project

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