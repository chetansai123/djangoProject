from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'home/index.html')
    # return HttpResponse("This is Home  Page of Home APP")


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def services(request):
    return render(request, 'home/services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        checkbox = request.POST.get('checkbox')
        contact = Contact(name=name, email=email, phone=phone,Desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your data has been added to database")
        # messages.discard()
    return render(request, 'home/contact.html')
