from django.shortcuts import render
import random

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def variable(request):
   x = 5 # create a variable called x and give it a value
   y = 10
   # pass the variable x to the template variable.html with the name 'x'
   return render(request, 'variable.html', {'x': x, 'y': y })


def randomnumber(request):
   x = random.randint(0,100) # generate a random number between 0 and 100
   return render(request,'random.html',{'x':x})

def loop(request):
    nums = list(range(1, 31))
    return render(request, 'ex2.html', {'nums': nums})
