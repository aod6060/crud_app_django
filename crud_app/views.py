from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.template import loader

from .models import Message

# Create your views here.
def index(request: HttpRequest):
    #return HttpResponse("Hello, World. You're at the crud index.")
    messages = Message.objects.order_by('id')
    temp = loader.get_template("crud/index.html")
    context = {
        "messages": messages,
    }
    return HttpResponse(temp.render(context, request))

def new(request: HttpRequest):
    temp = loader.get_template("crud/new.html")
    context = {}
    return HttpResponse(temp.render(context, request))

def new_post(request: HttpRequest):
    if request.POST.get("message") == "":
        return HttpResponseRedirect("/new")
    else:
        temp = Message.objects.create()
        temp.message = request.POST.get("message")
        temp.save()
        return HttpResponseRedirect("/")
    
def edit(request: HttpRequest, id:int):
    message = Message.objects.get(id=id)
    temp = loader.get_template("crud/edit.html")
    context = {
        "message": message
    }
    return HttpResponse(temp.render(context, request))

def edit_post(request: HttpRequest, id:int):
    temp = Message.objects.get(id=id)
    temp.message = request.POST.get("message")
    temp.save()
    return HttpResponseRedirect("/edit/"+str(id)+"/")


def delete(request: HttpRequest, id:int):
    message = Message.objects.get(id=id)
    temp = loader.get_template("crud/delete.html")
    context = {
        "message": message
    }
    return HttpResponse(temp.render(context, request))

def delete_post(request: HttpRequest, id:int):
    temp = Message.objects.get(id=id)
    temp.delete()
    return HttpResponseRedirect("/")
