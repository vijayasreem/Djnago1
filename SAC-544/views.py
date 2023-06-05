from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import JiraForm
from .models import Jira

# Create your views here.
@login_required
def configure_jira(request):
    if request.method == 'POST':
        form = JiraForm(request.POST)
        if form.is_valid():
            jira = Jira.objects.create(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password'],
                url=form.cleaned_data['url'],
                repository_name=form.cleaned_data['repository_name']
            )
            jira.save()
            messages.success(request, f'Jira Software successfully configured!')
            return render(request, 'jira.html', {'form': form})
    else:
        form = JiraForm()
    jiras = Jira.objects.all()
    return render(request, 'jira.html', {'form': form, 'jiras': jiras})

@csrf_protect
def jira_edit(request, id):
    jira = Jira.objects.get(pk=id)
    if request.method == 'POST':
        form = JiraForm(request.POST, instance=jira)
        if form.is_valid():
            jira.username = form.cleaned_data['username']
            jira.password = form.cleaned_data['password']
            jira.url = form.cleaned_data['url']
            jira.repository_name = form.cleaned_data['repository_name']
            jira.save()
            messages.success(request, f'Jira Software successfully updated!')
            return render(request, 'jira.html', {'form': form})
    else:
        form = JiraForm(instance=jira)
    return render(request, 'jira_edit.html', {'form': form})

@csrf_protect
def jira_delete(request, id):
    jira = Jira.objects.get(pk=id)
    jira.delete()
    messages.success(request, f'Jira Software successfully deleted!')
    return render(request, 'jira.html')