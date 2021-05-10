from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def close(request):
    return render(request, 'close.html')
