from django.shortcuts import render
from user_interface.models import Type, Unit

def index(request):
    types = Type.objects.all()
    context = {"types": types}
    return render(request, "index.html", context)

def conversion_types(request, type):
    units = Unit.objects.filter(type__measurement__contains=type)
    context = {"units": units}
    return render(request, "conversion_types.html", context)
