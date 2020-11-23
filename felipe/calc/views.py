from django.shortcuts import render
import requests  # API call icin => pip install requests yapildi 


from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the calc index.")
def api(request, *args, **kwargs):
    response = requests.get("https://api.covid19api.com/countries").json
    return render(request, "api.html", {"response":response} )

def styles(request, *args, **kwargs):
    return render(request, "style-try.html", {} )

    
def index(request, *args, **kwargs ):
    mycontext = {
        "my_text": "This is my Django code",
        "my_number": 11,
        "my_day": "Friday",
        "my_list": [111,222,333,444,555,666,777]
        }

    return render(request, "about.html", mycontext )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, *args, **kwargs):
    # return HttpResponse("You're voting on question %s." % question_id)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "vote.html", {} )

def fehmi(request, *args, **kwargs):
    # return HttpResponse("You're voting on question %s." % question_id)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "fehmi.html", {} )

