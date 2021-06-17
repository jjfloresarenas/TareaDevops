from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponseNotFound("Hello World!")
