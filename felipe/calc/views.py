from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the calc index.")
    
def index(request,*args, **kwargs ):
    return render(request, "about.html", {} )

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, *args, **kwargs):
    # return HttpResponse("You're voting on question %s." % question_id)
    # return HttpResponse("<h1>Hello World!</h1>")
    return render(request, "vote.html", {} )
