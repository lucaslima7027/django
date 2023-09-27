from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "streaming_vod/index.html")

def greet(request, name):
    return render(request, "streaming_vod/greet.html", {"name":name.capitalize()})

tasks = ["foo", "bar", "baz"]
def index1(request):
    return render(request, "streaming_vod/tasks.html", {
        "tasks": tasks
        })

def add(request):
    return render(request, "streaming_vod/add.html")