from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(Request):
    return render(Request, "streaming_vod/index.html")

def greet(Request, name):
    return HttpResponse(f"Helo {name}")