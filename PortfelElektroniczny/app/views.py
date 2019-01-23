"""
Definition of views.
"""

from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import Rejestracja
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app.models import Wallet
from app.models import Post
from django.utils import timezone
from django.views.generic import CreateView



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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'O aplikacji',
            'posts': posts,
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
    form = UserCreationForm()
    return render(
        request,
        'app/rejestracja.html',
        {
            'title':'Tworzenie konta',
            'form' : form,
            'year':datetime.now().year,
        }
    )
class Register(CreateView):
    form_class = Rejestracja
    #template_name = "account/register.html"
 
    def form_valid(self, form):
        form.save()
 
        user = authenticate(username=form.cleaned_data.get("username"),
                            password=form.cleaned_data.get("password1"))
        login(self.request, user)
 
        return redirect("about")