from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import TeamForm
from .models import FootballTeam

def team_create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Oops, something went wrong, nothing was created")

    # if request.method == "POST":
    #     print request.POST.get("name")
    #     print request.POST.get("points_total")
    context = {"form": form,}
    return render(request, "team_form.html", context)

def team_detail(request, id):
    instance = get_object_or_404(FootballTeam, id=id)
    context = {"title": instance.name, "instance": instance,}
    return render(request, "team_detail.html", context)
    # return HttpResponse("<h1>Detail</h1>")

def team_list(request):
    queryset = FootballTeam.objects.all()
    context = {"object_list": queryset, "title": "List"}
    return render(request, 'index.html', context)
    # return HttpResponse("<h1>List</h1>")

def team_update(request, id):
    instance = get_object_or_404(FootballTeam, id=id)
    form = TeamForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"title": instance.name, "instance": instance, "form": form,}
    return render(request, "team_form.html", context)

def team_delete(request):
    return HttpResponse("<h1>Delete</h1>")
