from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render(request, "index.html")

def contactview(request):
    return render(request, "contact.html")

def homeview(request):
    return render(request, "home.html")