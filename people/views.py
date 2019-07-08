from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
import plivo
import random

from django.views.decorators.csrf import csrf_exempt


from plivo import plivoxml

# Create your views here.
@csrf_exempt
def replySMS(request):
    client = plivo.RestClient(auth_id='', auth_token='')
    from_number = request.POST.get('From')
    text = request.POST.get('Text')
    text = text.lower()

    jobs = ['welfare checks', 'creek sandbagging ', ' evacuee setup ', ' donation sorting ']
    descripts = [' Welfare checking is where you go door to door making sure that everyone has been able to evacuate. It requires the ability to climb stairs and talk to others. ',
                ' Sandbagging is where one lifts bags filled with sand to form a barrier which stops water. It requires a great deal of physical fitness and the ability to work in a team. ',
                 ' Evacuee setup is where evacuation centres are prepared with cots, food, and other essentials for the arrival of people displaced by flooding. It requires the ability to lift light items and work in a team. ',
                 ' Donation sorting is where boxes of physical donations are processed. It requires the ability to lift light items. ']

    message = ""
    address = ['101 Peter St ', '3205 Unity Dr', '100 Queen St W']
    if "go" in text:
        message = "Hi there. A state of local emergency has been declared due to flooding in Downtown Toronto. Are you available to help?"
    elif "yes" in text:
        x = random.randint(0,4)
        message = "Great, thank you. We need your help conducting {} . {}. Text 'ready' if you can do this or 'sorry' if you can't. ".format(jobs[x],descripts[x])
    elif 'ready' in text:
        message = "Excellent. Report to {} and text 'arrived' when you get there.".format(random.choice(address))
    elif 'sorry' in text:
        message = "Thanks anyway. We will find something else for you to do."

    response = client.messages.create(
        src='16475602585',
        dst=from_number,
        text=message, )
    return HttpResponse(response, content_type="text/xml")


def index(request):
    context = {
        'payload': 0
    }
    return render(request, 'people/index.html', context)
def enroll(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully signed up")
    else:
        form = PersonForm()
    context = {
        'form': form,
    }

    return render(request, 'people/enrollment.html', context)

def emergency(request):
    if request.method == 'POST':
        form = EmergencyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully created emergency")
    else:
        form = EmergencyForm()
    context = {
        'form': form,
    }

    return render(request, 'people/emergency.html', context)

def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully created task")
    else:
        form = TaskForm()
    context = {
        'form': form,
    }

    return render(request, 'people/task.html', context)
