from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em> Second Project</em>")

def help(request):
    helpdict = {"help_insert": "Help page"}
    return render(request, 'AppTwo/help.html', context = helpdict)
