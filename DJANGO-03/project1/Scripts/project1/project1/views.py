from django.http import HttpResponse

def function(request):
    return HttpResponse('<b><h1>This is my </h1></b>')
