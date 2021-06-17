from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Hello World!")
