from django.http import HttpResponse
import datetime

def saludo(request):   # primera vista

    documento = """<html>
    <body>
    <h1>
    Hello world, this is my first web page with Django!
    </h1>
    </body>
    </html>"""

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("See you soon")

def dameFecha(request):

    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actaules: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)