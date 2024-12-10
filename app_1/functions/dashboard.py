from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app_1.models import *

@login_required
def dashboard (request):
    contexto = {}
    contexto['famosos'] = Productos.objects.all()
    return render(request,'dashboard.html',contexto)
    