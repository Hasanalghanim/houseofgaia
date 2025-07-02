from django.contrib.sitemaps.views import sitemap  # Import the correct sitemap view
from django.urls import path,include
from django.views.generic import RedirectView


from . import views


urlpatterns = [
    path('', views.enter_code, name='enter_code'),
    path('appointments', views.booking_page, name='appointments'),
]
