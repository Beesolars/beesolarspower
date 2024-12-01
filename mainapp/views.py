from django.shortcuts import render
# Create your views here.


def homepage(request):
    return render(request,"tempsfiles/index.html")


def project(request):
    return render(request,"tempsfiles/projects.html")