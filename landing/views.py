from django.shortcuts import render

# [/]: home
def index(request):
    return render(request, 'landing/index.html')
