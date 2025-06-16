from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class BlogPost(models.Model): 
    title = models.CharField(max_length=75)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=200) 
    summary = models.CharField(max_length=500, null=True) 
    body = RichTextField()

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
    def save(self, *args, **kwargs):
        if not self.slug:
           
            self.slug = slugify(self.title)
            
           
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.title)}-{BlogPost.objects.filter(slug=self.slug).count() + 1}"

        super().save(*args, **kwargs)


    

    def __str__(self):
        return self.title