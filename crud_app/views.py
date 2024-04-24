from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Message

# Create your views here.
def index(request):
    #return HttpResponse("Hello, World. You're at the crud index.")
    messages = Message.objects.order_by('id')
    temp = loader.get_template("crud/index.html")
    context = {
        "messages": messages,
    }
    return HttpResponse(temp.render(context, request))
