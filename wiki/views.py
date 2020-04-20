from django.shortcuts import render
from script.wikipedia import run

def main(request):
    return render(request, 'main.html', {})

def wiki(request):
    run()
    return render(request, 'main.html', {})
# Create your views here.
