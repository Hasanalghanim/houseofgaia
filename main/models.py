import requests
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from hitcount.models import HitCount
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill



class LandingPage(models.Model):
    name = models.CharField(max_length=100, default="landing")
    test = models.CharField(max_length=100, default="landing")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')


class AboutPage(models.Model):
    name = models.CharField(max_length=100, default="aboutPage")
    test = models.CharField(max_length=100, default="aboutPage")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')

class AllBlogsPage(models.Model):
    name = models.CharField(max_length=100, default="AllBlogsPage")
    test = models.CharField(max_length=100, default="AllBlogsPage")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')




class BlogPost(models.Model): 
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=200) 
    summary = models.CharField(max_length=500, null=True) 
    body = RichTextField()


    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk')
    test = models.CharField(max_length=100, default="blogpost")
    image_hero_large = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1200, 500)],  
        format='JPEG',
        options={'quality': 90}
    )
    
    
    image_hero_small = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 300)],  
        format='JPEG',
        options={'quality': 80}
    )
    
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(150, 150)],  
        format='JPEG',
        options={'quality': 80}
    )


    def get_absolute_url(self):
        return reverse('blogDetail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
           
            self.slug = slugify(self.title)
            
           
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{BlogPost.objects.filter(slug=self.slug).count() + 1}"



        try:
            sitemap_url = f"https://www.houseofgaia.ca/sitemap.xml"
            requests.get(f"https://www.google.com/ping?sitemap={sitemap_url}", timeout=5)
            requests.get(f"https://www.bing.com/ping?sitemap={sitemap_url}", timeout=5)
        except requests.RequestException:
            pass 
        super().save(*args, **kwargs)


    

    def __str__(self):
        return self.title
    




