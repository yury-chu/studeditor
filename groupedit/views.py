from django.shortcuts import render, HttpResponseRedirect
from groupedit.forms import GroupForm
from studedit.models import Groups

# Create your views here.


def show(request):
    groups = Groups.objects.all()
    args = {
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