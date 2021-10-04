from  django.http import HttpResponse
from django.shortcuts import render
import operator

def dash(request):
    return render(request,'dash.html')