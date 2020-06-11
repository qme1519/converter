from user_interface.models import Type, Unit, BaseUnit, History
from user_interface.forms import UnitConversion, LogInForm, DateConverter
from user_interface.currency_conversion import update_current_exchange_rates
from datetime import datetime
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # get all conversions available
    types = Type.objects.all()
    context = {"types": types}

    # if user is logged in, display last 10 queries
    if request.user.is_authenticated:
        queries = History.objects.filter(user__exact=request.user).order_by('-timestamp')[:10]
        context['queries'] = queries

    return render(request, "index.html", context)

def conversion_types(request, type, pk=-1):
    try:
        context = {}
        context['history'] = 'false'
        context['message'] = 'false'
        if pk != -1:
            # user query needs to be retrieved
            if request.user.is_authenticated:
                user_query = History.objects.get(pk=pk)
                if user_query.user == request.user:
                    # only retrieve query if it belongs to the user
                    context['history'] = 'true'
                    context['query'] = user_query
                else:
                    return HttpResponse("This query does not belong to this account")
            else:
                return HttpResponse("You are not logged in")
        if request.method == "POST":
            # user submitted a query
            if request.user.is_authenticated:
                # execute if user is logged in
                try:
                    # retireve all the values from the post data, process it
                    source_unit = request.POST['source_unit'].split(" ")[0]
                    source_value = request.POST['source_value']
                    destination_unit = request.POST['destination_unit'].split(" ")[0]
                    destination_value = request.POST['destination_value']
                    History.objects.create(
                        timestamp=datetime.now().timestamp(),
                        source_unit=Unit.objects.get(unit=source_unit),
                        source_value=source_value,
                        destination_unit=Unit.objects.get(unit=destination_unit),
                        destination_value=destination_value,
                        type=Type.objects.get(measurement__contains=type),
                        user=request.user
                    )
                    context['message'] = 'Query successfully saved'
                except:
                    return HttpResponse("There's been a problem with saving this query")
            else:
                return HttpResponse("You are not logged in")

        # get all the units for this type of measurement
        units = Unit.objects.filter(type__measurement__contains=type)
        context['units'] = units
        context['type'] = type

        if type == "Currency":
            # if currency is to be converted, get the latest exchange rates
            timestamp = update_current_exchange_rates()
            last_updated = datetime.fromtimestamp(timestamp)
            unit_converter = UnitConversion()
            base_unit = BaseUnit.objects.get(type__measurement__contains=type)
            context["last_updated"] = str(last_updated)
            context['base_unit'] = base_unit
        elif type == "Date":
            # if date is to be converted, use a different user input form
            context["unit_converter"] = DateConverter()
            return render(request, "date_conversion.html", context)
        else:
            # standard conversion query
            unit_converter = UnitConversion()
            base_unit = BaseUnit.objects.get(type__measurement__contains=type)
            context['base_unit'] = base_unit

        context["unit_converter"] = unit_converter
        return render(request, "conversion_types.html", context)
    except:
        # returned if an invalid type of measurement or query ID has been entered
        return HttpResponse("Invalid query")

def signup_view(request):
    if request.method == 'POST':
        # user creation form completed
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if form is valid, save a new user
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        # user creation form needed
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return render(request, "login.html", {})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            form = LogInForm()
            context = {
                "message": "Invalid login details provided",
                "logged_in": "False",
                "form": form
            }
            return render(request, 'login.html', context)
    else:
        form = LogInForm()
        context = {
            "message": "",
            "logged_in": "False",
            "form": form
        }
        return render(request, 'login.html', context)

def log_out_view(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'logout.html', {})
    else:
        return HttpResponse("You are not logged in and so cannot log out")

def user_history(request):
    if request.user.is_authenticated:
        queries = History.objects.filter(user__exact=request.user)
        context = {'queries': queries, 'user': request.user}
        return render(request, 'history.html', context)
    else:
        return HttpResponse("You are not logged in")
