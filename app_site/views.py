from django.shortcuts import render, redirect
from django.contrib import messages
from app_site.models import Messages
import datetime


# Create your views here.
def home(request):
    return render(request, 'my_website/about.html')

def about(request):
    return render(request, 'my_website/about.html')

def skills(request):
    return render(request, 'my_website/skills.html')

def career(request):
    return render(request, 'my_website/career.html')

def projects(request):
    return render(request, 'my_website/projects.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['sender-name']
        msg = request.POST['sender-msg']
        pub_date = datetime.date.today()    # for time-stamping

        if name == "":
            messages.info(request, 'you forgot to include your name')
            return redirect('/contact')
        elif msg == "":
            messages.info(request, 'no messages sent')
            return redirect('/contact')
        else:
            comments = Messages.objects.create(name=name, msg=msg, pub_date=pub_date)
            comments.save();
    
    else:
        msgs = Messages.objects.all()        
        return render(request, 'my_website/contact.html', {'msgs': msgs})
    
    return redirect('/contact')