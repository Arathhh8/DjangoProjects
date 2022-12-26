from django.http import HttpResponse

def saludo(request):   # primera vista

    return HttpResponse("Hello world, this is my first web page with Django!")