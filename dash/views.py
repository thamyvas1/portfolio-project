from django.shortcuts import render
from .models import Dash

def dash(request):
    dashs = Dash.objects
    return render(request, 'dash/dash.html', {'dash': dashs})