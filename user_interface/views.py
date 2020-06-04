from django.shortcuts import render
from user_interface.models import Type

def index(request):
    types = Type.objects.all()
    context = {"types": types}
    return render(request, "index.html", context)
