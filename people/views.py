from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. Flood volunteers shall be organized.")

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