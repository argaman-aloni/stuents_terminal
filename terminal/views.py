from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """This function will create a simple view with django."""
    return HttpResponse("Hello, world. You're at the terminal's index!!")