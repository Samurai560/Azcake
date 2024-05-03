from django.shortcuts import render, HttpResponse
from .models import Cake





def home(request):
    cakes = Cake.objects.all()
    context = {
        "tortlar": cakes
    }
    return render(request, "cakes/home.html", context)


def tortlar_view(request, pk):
    cake = Cake.objects.get(id=pk)
    context = {
        "pinqvin": cake
    }
    return render(request, "cakes/cake_details.html", context)


def contact(request):
    return render(request, "cakes/contact.html",)


def about(request):
    return render(request, "cakes/about.html",)

def populyar(request):
    cakes = Cake.objects.filter(rating__gte=3)
    context = {
        "tortlar": cakes,
    }
    return render(request, "cakes/populyar.html", context)




def home(request):
    cakes = Cake.objects.order_by("price")
    context = {
        "tortlar": cakes,
    }
    return render(request, "cakes/contact.html",)





