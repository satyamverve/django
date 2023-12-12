from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse

def members(request):
    template = loader.get_template('index.html')
    # return HttpResponse("Hello world!")
    return HttpResponse(template.render())
