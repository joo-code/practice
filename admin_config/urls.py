"""admin_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import BRAND

from BRAND import views
from CRM import views
from KFQ import views

urlpatterns = [
    path('',BRAND.views.theme_index),
    # path('',KFQ.views.Date2021_06_22.no_01),
    path('admin/', admin.site.urls),

    #Brand 관련 페이지
    # path('BRAND/', BRAND.views.index),
    path('BRAND/', include('BRAND.urls')),


    #CRM system 관련 페이지
    path('CRM/', include('CRM.urls')),


    #한국품질재단 교육
    path('KFQ/', include('KFQ.urls')),
]
