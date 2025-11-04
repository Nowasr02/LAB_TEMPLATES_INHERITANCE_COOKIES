from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request : HttpRequest):
    
    return render(request, "realEstate_web/home.html")


def properties(request : HttpRequest):
    
    return render(request, "realEstate_web/properties.html")


def contact(request : HttpRequest):
    
    return render(request, "realEstate_web/contact.html")

def toggle_dark_mode(request : HttpRequest):

    current = request.session.get('dark_mode', False)
    request.session['dark mode'] = not current
    messages.success(request, 'Dark mode preference updated. ')
    
    return redirect('/')