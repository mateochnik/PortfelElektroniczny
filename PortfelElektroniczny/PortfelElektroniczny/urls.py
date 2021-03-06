"""
Definition of urls for PortfelElektroniczny.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.urls import path


import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^dochody$', app.views.dochody, name='dochody'),
    url(r'^bilans$', app.views.bilans, name='bilans'),
    url(r'^wydatki$', app.views.wydatki, name='wydatki'),
    url(r'^rejestracja$', app.views.rejestracja, name='rejestracja'),
    url(r'^dodajDochod$', app.views.dodajDochod, name='dodajDochod'),
    url(r'^dodajWydatek$', app.views.dodajWydatek, name='dodajWydatek'),
   
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Zaloguj',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    path('post/new', views.post_new, name='post_new'),
]
