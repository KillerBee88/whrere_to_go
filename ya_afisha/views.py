from django.http import HttpResponse
from django.shortcuts import render

def where_to_go(request):
    return render(request, 'index.html')