from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def createReceipe(request):
    if(request.method == 'POST'):
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_desc = data.get("receipe_desc")
        receipe_img = request.FILES.get("receipe_img")


        Veggie.objects.create(
            receipe_name = receipe_name,
            receipe_desc = receipe_desc,
            receipe_img = receipe_img
        )

        return redirect("/show-receipe-list/")

    return render(request,"receipe.html")



def showReceipeList(request):
    receipeList = Veggie.objects.all();
    context = {"receipeList" : receipeList}
    for _item in receipeList:
        print("--->>>>>>>.",_item.receipe_img)
    return render(request, "receipe_list.html", context)


def deleteReceipe(request,id):
    Veggie.objects.get(id=id).delete()
    return redirect("/show-receipe-list/")