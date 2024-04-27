from django.shortcuts import render
from django.http import JsonResponse
from Django.models import Personas
from datetime import datetime


# Create your views here.
def select (request):
    result = Personas.objects.all()
    return JsonResponse(result)

def update (request):
      

    if request.method == 'POST':
      firstUser = Personas.objects.get(id=request.POST.get('id'))
      Personas.objects.filter(id=request.POST.get('id')).update(name=request.POST.get('name'), age = request.POST.get('age'), date = request.POST.get('date'), update=datetime.now())
      result = {'info': f'los datos de la persona {firstUser.id} han sido actualizados'}
      return JsonResponse(result)


def insert (request):
    if request.method == 'POST':
     
      Personas.objects.create(name=request.POST.get('name'), age=request.POST.get('age'), date=request.POST.get('date'), time=datetime.now())

      data = {'info':"el usuario fue agregado exitosamente"}
      return JsonResponse(data)
    return JsonResponse()

def delete(request):
    if request.method == 'POST':
      Personas.objects.filter(id=request.POST.get('id')).delete()

      data = {'info':"el usuario fue eliminado "}

      return JsonResponse(data)
    return JsonResponse()