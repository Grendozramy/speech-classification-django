from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.urls import reverse

from .models import Message

# Create your views here.
def index(request):
    messages = Message.objects.all()
    context = {
        'messages': messages
    }

    return render(request, 'message/index.html', context)

def create(request):
    return render(request, 'message/create.html')

def store(request):
    nim = request.POST['nim']
    name = request.POST['name']
    word = request.POST['word']
    id = None
    messages = Message(id, nim,name,word)
    messages.save()

    return redirect('/message/')
    
def detail(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'message/detail.html', {"message": message})

def edit(request, id):
    message = Message.objects.get(id=id)
    return render(request, 'message/edit.html', {"message": message})


def update(request, id):
    message = Message.objects.get(id=id)
    message.nim = request.POST['nim']
    message.name = request.POST['name']
    message.word = request.POST['word']
    message.save()

    return redirect('/message/', id)

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    
    return redirect('/message/')