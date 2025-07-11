
from django.contrib.sitemaps.views import sitemap  # Import the correct sitemap view
from django.urls import path,include
from django.views.generic import RedirectView

from . import sitemap as custom_sitemap
from . import views

# Define your sitemaps
sitemaps = {
    'static': custom_sitemap.StaticViewSitemap, 
    'blogs': custom_sitemap.BlogSitemap,
    'piercings': custom_sitemap.ServicesSitemap,
}


urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('redirect/', RedirectView.as_view(url='/', permanent=False), name='redirect_to_home'),
    path('about', views.about, name='about'),
    path('piercings/', include('services.urls') ),
    path('the-piercing-edit/', views.allBlogs, name='allBlogs'),
    path('the-piercing-edit/<slug:slug>/',views.blogDetail, name='blogDetail'),


    path('booking/',include('booking.urls')),


    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name="sitemap"),  
]
