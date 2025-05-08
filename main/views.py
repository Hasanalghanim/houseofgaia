from django.shortcuts import render


# Create your views here.
def landingPage(request):

    # return render(request, "coming_soon.html",)
    return render(request, "landingPage.html",)



# Create your views here.
def about(request):

    # return render(request, "coming_soon.html",)
    return render(request, "about.html",)

