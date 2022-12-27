from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido = apellido

def saludo(request):   # primera vista

    p1 = Persona(" Ing. Arath"," García")

    #nombre = "Arath"
    #apellido = "García"

    actual = datetime.datetime.now()

    doc_externo = open("C:/Users/arath/Documents/DjangoProjects/Project1/Project1/plantillas/plantilla1.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora_actual":actual})

    #RENDERIZAR DOCUMENTO

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("See you soon!!!")

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

def calculaEdad(request, edad, year):

    #edadActual = 18
    periodo = year - 2022
    edadFutura = edad + periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(year, edadFutura)

    return HttpResponse(documento)



