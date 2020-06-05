from django.shortcuts import render
from user_interface.models import Type, Unit
from user_interface.forms import UnitConversion

def index(request):
    types = Type.objects.all()
    context = {"types": types}
    return render(request, "index.html", context)

def conversion_types(request, type):
    units = Unit.objects.filter(type__measurement__contains=type)
    if request.method == "POST":
        pass
    else:
        unit_converter = UnitConversion()
    context = {"units": units, "type": type, "unit_converter": unit_converter}
    return render(request, "conversion_types.html", context)
