from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

from django.contrib.auth.models import User

from .forms import RegisterForm

def index(request):
    return render(request,"index.html",{
    "message": "Listado de productos",
    "title": "Productos",
    'products': [
        {"title":"Playera","price":5,"stock":True},
        {"title":"Camisa","price":7,"stock":True},
        {"title":"Mochila","price":20,"stock":False},
        {"title":"Laptop","price":500,"stock":True}
         #producto
    ]
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Bienvenido {}".format(user.username))
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña no validos")

    return render(request, "users/login.html",{

    })


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada exitosamente")
    return redirect ("login")


def register(request):
    form = RegisterForm(request.POST or None )

    if request.method=="POST" and form.is_valid():
        username = form.cleaned_data.get("username", None)
        email = form.cleaned_data.get("email", None)
        password = form.cleaned_data.get("password", None)


        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            message.success(request, "Usuario creado exitosamente")
            return redirect("index")

    return render(request, "users/register.html",{
        "form": form

    })
