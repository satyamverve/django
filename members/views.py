from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Member
# Create your views here.
from django.http import HttpResponse

def members(request):
    mymembers= Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {             #Creates an object containing the mymembers object to send the object to template
    'mymembers': mymembers,
    }
    # return HttpResponse("Hello world!")
    return HttpResponse(template.render(context, request))

def details(request, id):    #Gets the id as an argument.
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,   
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

