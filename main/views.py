from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import BlogPost


def landingPage(request):
    posts = BlogPost.objects.order_by('-id')[:3] 
    return render(request, "landingPage.html", {'blogs': posts})



# Create your views here.
def about(request):
    return render(request, "about.html",)


def allBlogs(request):
    posts = BlogPost.objects.order_by('-id') 
    return render(request, "allBlogs.html", {'blogs': posts})


def blogDetail(request,slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blogDetail.html", {"blog": blog})





def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://houseofgaia.ca/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")