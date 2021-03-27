from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,"index.html")


def technology(request):

    return render(request,"technology.html")
