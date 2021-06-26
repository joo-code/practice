from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("BRAND PAGE.")

def template_index(request):
    print("PAGE : template_index")
    return render(request, './brand/1_index.html')
#***********************************************************************#
# Original Theme
def theme_index(request):
    print("PAGE : theme_index")
    page ='Home'
    context = {
        'page' : page
    }
    return render(request, './theme/1_index.html', context)

def theme_aboutus(request):
    print("PAGE : theme_about")
    page = 'About Us'
    context = {
        'page': page
    }
    return render(request, './theme/2_about.html', context)

def theme_features(request):
    print("PAGE : theme_features")
    page = 'Features'
    context = {
        'page': page
    }
    return render(request, './theme/3_features.html', context)

def theme_hosting(request):
    print("PAGE : theme_hosting")
    page = 'Hosting'
    context = {
        'page': page
    }
    return render(request, './theme/4_hosting.html', context)

def theme_domain(request):
    print("PAGE : theme_domain")
    page = 'Domain'
    context = {
        'page': page
    }
    return render(request, './theme/5_domain.html', context)

def theme_pricing(request):
    print("PAGE : theme_domain")
    page = 'Pricing'
    context = {
        'page': page
    }
    return render(request, './theme/6_pricing.html', context)

def theme_contact(request):
    print("PAGE : theme_contact")
    page = 'Contact'
    context = {
        'page': page
    }
    return render(request, './theme/7_contact.html', context)
#***********************************************************************#
