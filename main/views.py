from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import BlogPost,LandingPage


from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


def landingPage(request):
    posts = BlogPost.objects.order_by('-id')[:3] 

    landing = LandingPage.objects.get(name="landing")
    hit_count = HitCount.objects.get_for_object(landing)
    HitCountMixin.hit_count(request, hit_count)

    return render(request, "landingPage.html", {'blogs': posts, 'hit_count':hit_count.hits})



# Create your views here.
def about(request):
    return render(request, "about.html",)


def allBlogs(request):
    posts = BlogPost.objects.order_by('-id') 
    return render(request, "allBlogs.html", {'blogs': posts})


def blogDetail(request,slug):
    blog = get_object_or_404(BlogPost, slug=slug)

    hit_count = HitCount.objects.get_for_object(blog)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)

    return render(request, "blogDetail.html", {"blog": blog, 'hit_count':hit_count.hits})






def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://houseofgaia.ca/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")