from django.contrib import admin

from .models import Service,Jewelry,AllServicesPage


admin.site.register(AllServicesPage)
admin.site.register(Service)
admin.site.register(Jewelry)