from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from hitcount.models import HitCount
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.urls import reverse


class AllServicesPage(models.Model):
    name = models.CharField(max_length=100, default="AllServicesPage")
    test = models.CharField(max_length=100, default="AllServicesPage")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    imageLeft = models.ImageField(upload_to='images/', blank=True)
    
    image_hero_large_left = ImageSpecField(
        source='imageLeft',
        processors=[ResizeToFill(1200, 500)],  
        format='PNG',
        options={'quality': 90}
    )
    

class Service(models.Model): 
    title = models.CharField(max_length=75)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    order = models.IntegerField()
    image_hero_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(500, 1200)],  
        format='PNG',
        options={'quality': 90}
    )
    
    
    image_hero_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 280)],  
        format='PNG',
        options={'quality': 80}
    )
    
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(150, 150)],  
        format='PNG',
        options={'quality': 80}
    )
    def get_absolute_url(self):
        return reverse('serviceDetail', kwargs={'title': self.title})
    def __str__(self):
        return self.title
    

class Jewelry(models.Model):
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='jewelry_images/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)
    quantity_in_stock = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    services = models.ManyToManyField(Service, related_name='jewelry_items')
    
    image_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],  
        format='JPEG',
        options={'quality': 80}
    )

    def __str__(self):
        return self.name