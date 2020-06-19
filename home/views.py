from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect
from django_otp import util


# Create your views here.


def index(request):
    return redirect("/accounts/login")


def welcome(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home/index.html')
    else:
        raise Http404
