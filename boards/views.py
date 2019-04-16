# Handle request/response cycle of web app
from django.shortcuts import render
from django.http import HttpResponse

def home(requset):
    return HttpResponse('Welcome, Board!')
