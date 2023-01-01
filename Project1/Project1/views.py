from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido = apellido

def saludo(request):   # primera vista

    p1 = Persona(" Ing. Arath "," García")

    #nombre = "Arath"
    #apellido = "García"
    temasDelCurso = ["Boostrap","Templates","Filtros"]

    actual = datetime.datetime.now()

    #doc_externo = open("C:/Users/arath/Documents/DjangoProjects/Project1/Project1/plantillas/plantilla1.html")
    #plt = Template(doc_externo.read())
    #doc_externo.close()

    #doc_externo = get_template('platila1.html')

    #ctx = Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora_actual":actual, "temas":temasDelCurso})

    #RENDERIZAR DOCUMENTO

    #documento =doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora_actual":actual, "temas":temasDelCurso})

    return render(request, "plantilla1.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "ahora_actual":actual, "temas":temasDelCurso})

def despedida(request):

    return HttpResponse("See you soon!!!!!")

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



