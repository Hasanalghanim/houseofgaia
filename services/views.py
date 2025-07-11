from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from .models import Service,AllServicesPage





def allServices(request):
    allServices = Service.objects.order_by('order') 
    heroPhotos = AllServicesPage.objects.all()
    print(heroPhotos)
    return render(request, "allServices.html", {'allServices':allServices,'heroPhotos':heroPhotos})

def serviceDetail(request,title):
    blog = get_object_or_404(Service, title=title)



def serviceData(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        jewelry_items = service.jewelry_items.all() 
        
        
        jewelry_data = []

        for jewelry in jewelry_items:
            jewelry_info = {
                'name': jewelry.name,
                'material': jewelry.material,
                'price': jewelry.price,
                'image': jewelry.image_small.url  # Assuming 'image' field exists and you have an image URL
            }
            jewelry_data.append(jewelry_info)

        return JsonResponse(jewelry_data,safe=False)
    except Service.DoesNotExist:
        return JsonResponse({'error': 'Service not found'}, status=404)