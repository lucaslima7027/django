from django.http import HttpResponse
from django import forms
from django.shortcuts import render

class newTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.
def index(request):
    return render(request, "streaming_vod/index.html")

def greet(request, name):
    return render(request, "streaming_vod/greet.html", {"name":name.capitalize()})

tasks = []
def index1(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "streaming_vod/add.htm", {
                "form": form
            })
    return render(request, "streaming_vod/tasks.html", {
        "tasks": tasks,
        "form": newTaskForm()
        })