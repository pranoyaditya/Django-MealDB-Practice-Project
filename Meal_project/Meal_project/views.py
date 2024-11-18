from django.shortcuts import render

def direction(request):
    return render(request, 'home.html')