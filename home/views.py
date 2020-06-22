from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django_otp import util


# Create your views here.


def index(request):
    return redirect("/accounts/login")
    # return render(request, 'login/login.html')


def LDAPConnection(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home/index.html')
    else:
        raise Http404


def welcome(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home/index.html')
    else:
        raise Http404


def login(request):
    return render(request, 'login/login.html')


def login_user(request):
    username = password = ""
    state = ""

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'home.index.html', {'state': state, 'username': username})
        else:
            return render(request, 'login/login.html', {'state': state, 'username': username})
