from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Message

# Create your views here.
def index(request):
    message = Message.objects.all()
    context = {
        'messages': message
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

    return HttpResponseRedirect(reverse('message:index'))
    
def detail(request, id):
    message = get_object_or_404(Message, id=id)
    context = {
        'message': message
    }
     
    return render(request, 'message/detail.html', context)

def edit(request, id):
    message = get_object_or_404(Message, id=id)
    context = {
        'message': message
    }
    
    return render(request, 'message/edit.html', context)


def update(request, id):
    message = Message.objects.get(id=id)
    message.nim = request.POST['nim']
    message.name = request.POST['name']
    message.word = request.POST['word']
    message.save()

    return HttpResponseRedirect(reverse('message:index'))

def delete(request, id):
    message = get_object_or_404(Message, id=id)
    message.delete()
    
    return HttpResponseRedirect(reverse('message:index'))