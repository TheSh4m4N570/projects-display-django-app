from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects= Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(slug=pk)
    tags = project.tags.all()
    reviews = project.review_set.all()
    context = {'project':project, 'tags':tags, 'reviews':reviews}
    return render(request, 'projects/project.html', context)


@login_required(login_url="login")
def create_project(request):
    form = ProjectForm
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            return form
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    project = Project.objects.get(slug = pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        else:
            return form
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    project = Project.objects.get(slug=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'project': project}
    return render(request, 'projects/delete_template.html', context)
