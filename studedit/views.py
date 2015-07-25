from django.shortcuts import render, redirect
from studedit.models import Students, Senders
from studedit.forms import StudentForm
from django.contrib import auth

# Create your views here.
def user_now(request):
    user = auth.get_user(request)
    user_name = user.get_username()
    return user_name

####


def show_list(request):
    user_name = user_now(request)

    if user_name == 'super':
        students = Students.objects.all()
        message = "You see all"
    else:
        try:
            sender_obj = Senders.objects.get(name=user_name)
            students = Students.objects.filter(sender=sender_obj.id)
            message = 'your see you added students'
        except:
            message = 'You need enter in system'
            students = None

    args = {
        'students': students,
        'user_name': user_name,
        'message': message,
    }
    return render(request, 'studedit/students_list.html', args)


def add(request):
    form = StudentForm()
    user_name = user_now(request)
    args = {
        'form': form,
        'user_name': user_name,
    }
    return render(request, 'studedit/add_student.html', args)


def add_ok(request):
    push = StudentForm(request.POST)
    data = push.save(commit=False)
    user_name = user_now(request)
    data.sender = Senders.objects.get(name=user_name)
    push.save()
    return redirect('/studedit/')
