from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from hitcount.models import HitCount
from hitcount.views import HitCountMixin

from .models import AboutPage, AllBlogsPage, BlogPost, LandingPage
from services.models import Service


def landingPage(request):
    posts = BlogPost.objects.order_by('-id')[:3] 

    landing, created = LandingPage.objects.get_or_create(name="landing")
    hit_count = HitCount.objects.get_for_object(landing)
    allServices = Service.objects.all()
    HitCountMixin.hit_count(request, hit_count)

    return render(request, "landingPage.html", {'blogs': posts, 'hit_count': hit_count.hits,"allServices":allServices})



# Create your views here.
def about(request):
    aboutHits ,created = AboutPage.objects.get_or_create(name="aboutPage")
    hit_count = HitCount.objects.get_for_object(aboutHits)
    HitCountMixin.hit_count(request, hit_count)

    return render(request, "about.html", {'hit_count':hit_count.hits})







def allBlogs(request):
    posts = BlogPost.objects.order_by('-id') 


    blogHits ,created  = AllBlogsPage.objects.get_or_create(name="AllBlogsPage")
    
    hit_count = HitCount.objects.get_for_object(blogHits)
    HitCountMixin.hit_count(request, hit_count)
    
    return render(request, "allBlogs.html", {'blogs': posts,'hit_count':hit_count.hits})


def blogDetail(request,slug):
    blog = get_object_or_404(BlogPost, slug=slug)

    content_type = ContentType.objects.get_for_model(blog)
    hit_count, created = HitCount.objects.get_or_create(
        content_type=content_type,
        object_pk=blog.pk,
    )
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    return render(request, "blogDetail.html", {"blog": blog, 'hit_count':hit_count.hits})






def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://houseofgaia.ca/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")