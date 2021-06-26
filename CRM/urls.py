from django.urls import path

from CRM import views

urlpatterns = [
    path('test/', views.index),



#***********************************************************************#
    # Original Theme
    path('theme/index/', views.theme.theme_index, name='01_index.html'),
    path('theme/profile/', views.theme.theme_profile, name='02_profile.html'),
    path('theme/settings/', views.theme.theme_settings, name='03_settings.html'),
    path('theme/invoice/', views.theme.theme_invoice, name='04_invoice.html'),
    path('theme/blank/', views.theme.theme_blank, name='05_blank.html'),
    path('theme/UI_Element/page=<page>', views.theme.theme_UI_Element, name='06_UI_Element.html'),
    path('theme/icons/', views.theme.theme_icons, name='07_icons.html'),
    path('theme/forms/page=<page>', views.theme.theme_Forms, name='08_Forms.html'),
    path('theme/tables', views.theme.theme_tables, name='09_tables.html'),
    path('theme/charts', views.theme.theme_chart, name='10_charts.html'),
    path('theme/maps', views.theme.theme_maps, name='11_maps.html'),
    # path('theme//', views.index, name=''),
]