from django.urls import path

from BRAND import views

urlpatterns = [
    path('test/', views.index),
    path('template/index/', views.template_index, name='1_index.html'),
#***********************************************************************#
    # Original Theme
    path('theme/index/', views.theme_index, name='1_index.html'),
    path('theme/about/', views.theme_aboutus, name='2_about.html'),
    path('theme/features/', views.theme_features, name='3_features.html'),
    path('theme/hosting/', views.theme_hosting, name='4_hosting.html'),
    path('theme/domain/', views.theme_domain, name='5_domain.html'),
    path('theme/pricing/', views.theme_pricing, name='6_pricing.html'),
    path('theme/contact/', views.theme_contact, name='7_contact.html'),
#***********************************************************************#


]