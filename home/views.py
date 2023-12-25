from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return HttpResponse("Home page for dango server")


def about(request):
    return render(request, "index.html")


def infoList(request):
    arr = [
        {"name" : "John"},
        {"name" : "Aviek"}
    ];
    return HttpResponse([arr]);