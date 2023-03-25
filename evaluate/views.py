from django.shortcuts import render
from django.http import HttpResponse

# [/]: home
def index(request):
    return HttpResponse('Quiz reporting for duty!')
