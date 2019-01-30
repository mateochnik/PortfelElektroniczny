"""
Definition of views.
"""

from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import myUserCreationForm, DodajDochodForm, DodajWydatekForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from app.models import Wallet
from app.models import Post, Dochod, Wydatek
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
    
    dochod = Dochod.objects.all()
    
        
    return render(
        request,
        'app/dochody.html',
        {
            'title':'Dochody',
            'year':datetime.now().year,
            'dochod' : dochod
            
        }
    )

def wydatki(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    wydatek = Wydatek.objects.all()
    return render(
        request,
        'app/wydatki.html',
        {
            'title':'Wydatki',
            'year':datetime.now().year,
            'wydatek' : wydatek
            
        }
    )

def bilans(request):
    bilans = Wallet.objects.all()
    for bil in bilans:
        bil.obliczBilans
        balans = bil.current_balance
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/bilans.html',
        {
            'title':'Bilans',
            'year':datetime.now().year,
            'balans' : balans
        }
    )

def rejestracja(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'app/rejestracja.html', {'form': form})

def dodajDochod(request):
    if request.method == 'POST':
        print("ok")
        form = DodajDochodForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.amount = amount
            post.description = description
            post.category = category
            
            print("ok1")
    
            post.save()
            return redirect('dochod', pk=post.pk)
       
    else:
        form = DodajDochodForm()
        print("ok2")
    return render(request, 'app/dodajDochod.html', {'form': form})

def dodajWydatek(request):
    if request.method == 'POST':
        print("ok")
        form = DodajWydatekForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.amount = amount
            post.description = description
            post.category = category
            
            print("ok1")
    
            post.save()
            return redirect('wydatki', pk=post.pk)
       
    else:
        form =  DodajWydatekForm()
        print("ok2")
    return render(request, 'app/dodajWydatek.html', {'form': form})