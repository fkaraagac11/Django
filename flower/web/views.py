from django.shortcuts import render
import requests
# Create your views here.


def web(request, *args, **kwargs):
    return render(request, "web.html", {})
