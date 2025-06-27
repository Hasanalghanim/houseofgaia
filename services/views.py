from django.shortcuts import render
from django.http import JsonResponse

from .models import Service





def allServices(request):
    allServices = Service.objects.order_by('order') 

    return render(request, "allServices.html", {'allServices':allServices})




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