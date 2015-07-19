from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from studedit.models import Senders
# Create your views here.

def who(request):
    senders = Senders.objects.all()
    args = {
        'senders': senders
    }
    return render(request, 'authorisation/choice_sender.html', args)

def is_sender(request, sender_id):
    sender = Senders.objects.get(pk=sender_id)
    args = {
        'sender': sender
    }
    return render(request, 'authorisation/is_sender.html', args)

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User not found"
            return render (request, 'authorisation/login.html', args)
    else:
        return render(request, 'authorisation/login.html', args)

def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        new_curator_form = UserCreationForm(request.POST)
        if new_curator_form.is_valid():
            new_curator_form.save()
            new_curator = auth.authenticate(username=new_curator_form.cleaned_data['username'],
                                            password=new_curator_form.cleaned_data['password2'])
            auth.login(request, new_curator)
            return redirect('/')
        else:
            args['form'] = new_curator_form
    return render(request, 'authorisation/register.html', args)