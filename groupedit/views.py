from django.shortcuts import render, HttpResponseRedirect
from groupedit.forms import GroupForm
from studedit.models import Groups
from django.contrib import auth

# Create your views here.


def show(request):
    groups = Groups.objects.all()
    user_name = auth.get_user(request)
    args = {
        'user_name': user_name.get_username(),
        'groups': groups
    }
    return render(request, 'groupedit/group_list.html', args)

def add(request):
    form = GroupForm()
    args = {
        'form': form
    }
    return render(request, 'groupedit/add_group.html', args)

def add_ok(request):
    push = GroupForm(request.POST)
    push.save()
    return HttpResponseRedirect('/groupedit/show/')