from django.shortcuts import render, redirect
from authentications.models import SignupModel

# Create your views here.


def index(request):
    users = SignupModel.objects.all()
    return render(request, 'index.html', {'users': users})