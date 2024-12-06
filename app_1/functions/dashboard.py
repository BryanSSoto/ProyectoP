from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard (request):
    print('dashboard')
    return render(request,'dashboard.html')
    