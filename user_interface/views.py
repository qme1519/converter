from django.shortcuts import render
from user_interface.models import Type, Unit, BaseUnit
from user_interface.forms import UnitConversion
from user_interface.currency_conversion import update_current_exchange_rates
from datetime import datetime

def index(request):
    types = Type.objects.all()
    context = {"types": types}
    return render(request, "index.html", context)

def conversion_types(request, type):
    units = Unit.objects.filter(type__measurement__contains=type)
    base_unit_id = BaseUnit.objects.get(type__measurement__contains=type)
    context = {"units": units, "type": type, "base_unit": base_unit_id}
    if type == "Currency":
        timestamp = update_current_exchange_rates()
        last_updated = datetime.fromtimestamp(timestamp)
        context["last_updated"] = str(last_updated)
    if request.method == "POST":
        unit_converter = UnitConversion(request.POST)
    else:
        unit_converter = UnitConversion()


    context["unit_converter"] = unit_converter
    return render(request, "conversion_types.html", context)
