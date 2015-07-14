from django.shortcuts import render
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