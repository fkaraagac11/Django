from django.shortcuts import render
import requests

# Create your views here.


def webapp(request, *args, **kwargs):
    return render(request, "webapp.html", {})
