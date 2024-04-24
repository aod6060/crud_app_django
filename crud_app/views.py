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