from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(requests, nome, idade):
    return HttpResponse('<h1><a href="http://">Hello word! </a> Olá {} de {} anos </h1>'.format(nome, idade))