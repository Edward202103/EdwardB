from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (TemplateView)

                                

class Naruto(TemplateView):
    template_name='Naruto/naruto.html'    

class Home(TemplateView):
    template_name='home/home.html'        

class Demon(TemplateView):
    template_name='DemonSlayer/demon.html'

class Pokemon(TemplateView):
    template_name='Pokemon/pokemon.html'    

class MyHero(TemplateView):
    template_name='myHero/myHero.html'       

# def home(request):
#     return HttpResponse('Hello John')

# def momo(request):
#     return render(request, "about/about.html")