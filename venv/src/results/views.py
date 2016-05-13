from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import FootballTeam

def team_create(request):
    return HttpResponse("<h1>Create</h1>")

def team_detail(request, id=None):
    instance = get_object_or_404(FootballTeam, id=3)
    context = {"title": instance.name, "instance": instance,}
    return render(request, "team_detail.html", context)
    # return HttpResponse("<h1>Detail</h1>")

def team_list(request):
    queryset = FootballTeam.objects.all()
    context = {"object_list": queryset, "title": "List"}
    return render(request, 'index.html', context)
    # return HttpResponse("<h1>List</h1>")

def team_update(request):
    return HttpResponse("<h1>Update</h1>")

def team_delete(request):
    return HttpResponse("<h1>Delete</h1>")
