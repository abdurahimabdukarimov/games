from django.http import Http404
from django.shortcuts import render
from .models import Products, Comment, Video, Remot
# Create your views here.

def index(request):
    product = Products.objects.all()
    comments = Comment.objecvts.all()
    context = {
        "products": product,
        "comments": comments
    }
    return render(request, "index.html", context=context)

def about(request):
    return render(request, "about.html", context={})

def contact(request):
    return render(request, "contact.html", context={})

def product(request):
    video = Video.objects.all()
    remot = Remot.objects.all()
    context = {
        'video': video,
        'remot': remot
    }
    return render(request, "product.html", context=context)

def videodetailView(requests, id):
    try:
        video = Video.objects.get(id=id)
        context = {
            'video': video
        }
    except video.DoesNotExist:
        raise Http404("No car found")
    return render(requests, "videodetail.html", context=context)
def remotdetailView(requests, id):
    try:
        remot = Remot.objects.get(id=id)
        context = {
            'remot': remot
        }
    except remot.DoesNotExist:
        raise Http404("No remot found")
    return render(requests, "remotdetail.html", context=context)


def remot(request):
    return render(request, "remot.html", context={})

def video(request):
    video = Video.objects.all()
    context = {
        'video': video
    }
    return render(request, "video.html", context=context)



