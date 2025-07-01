
from django.contrib.sitemaps.views import sitemap  # Import the correct sitemap view
from django.urls import path,include
from django.views.generic import RedirectView


from . import views


urlpatterns = [
    path('', views.allServices, name='allServices'),
    path('/detail/<str:service_id>', views.serviceData, name='serviceData'),


 
]
