from django.shortcuts import render, HttpResponseRedirect
from studedit.models import Students, Senders
from studedit.forms import StudentForm
# Create your views here.

def show_list(request, sender_id):
    if sender_id == '1':
        students = Students.objects.all()
    else:
        students = Students.objects.filter(sender=sender_id)
    args = {
        'students': students,
        'sender': sender_id
    }
    return render(request, 'studedit/students_list.html', args)

def add(request, sender_id):
    form = StudentForm()
    args = {
        'form': form,
        'sender': sender_id,
    }
    return render(request, 'studedit/add_student.html', args)

def add_ok(request, sender_id):
    push = StudentForm(request.POST)
    data = push.save(commit=False)
    data.sender = Senders.objects.get(pk=sender_id)
    push.save()
    return HttpResponseRedirect('/studedit/%s/' % sender_id)
