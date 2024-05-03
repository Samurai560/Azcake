from django.urls import path
from django.core.mail import send_mail
from django.conf import settings
from .views import(
    home, 
    tortlar_view,
    contact,
    about,
    populyar,
   
    )


urlpatterns = [
    # id
    # pk - primary_key
    path("", home, name ="index"),
    path("contact/", contact, name ="contact"),
    path("tortlar/<int:pk>/", tortlar_view),
    path("about/", about, name ="about"),
    path("populyar/", populyar, name ="populyar"),

]




