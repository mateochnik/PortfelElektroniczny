"""
Definition of views.
"""

from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import Rejestracja
from django.contrib.auth import login, authenticate
from app.models import Wallet



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Strona glowna',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Moje konto',
            'message':'Witaj',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'O aplikacji',
           
            'year':datetime.now().year,
        }
    )

def dochody(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    model = Wallet.objects.all()
    for post in model:
        portfel = post
        
    return render(
        request,
        'app/dochody.html',
        {
            'title':'Dochody',
            'year':datetime.now().year,
            'portfel' : portfel
            
        }
    )

def wydatki(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/wydatki.html',
        {
            'title':'Wydatki',
            'year':datetime.now().year,
            
        }
    )

def bilans(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bilans.html',
        {
            'title':'Bilans',
            'year':datetime.now().year,
        }
    )

def rejestracja(request):    
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/rejestracja.html',
        {
            'title':'Tworzenie konta',
            'message':'Witajaaa',
            'year':datetime.now().year,
        }
    )
def wpisy(request):    
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/wpisy.html',
        {
            'title':'Zakladka: wpisy!',
            'year':datetime.now().year,
        }
    )