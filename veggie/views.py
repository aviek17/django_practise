from django.shortcuts import render
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_protect


# Create your views here.


@csrf_protect
def createReceipe(request):
    # print(request)
    if(request.method == 'POST'):
        print("---->>>>>>",request)
    return HttpResponse("veggies create receipe")

