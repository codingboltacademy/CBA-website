from django.urls import path,include
from .  import views

urlpatterns = [
    path("",views.indexview, name="index"),
    path("contact/",views.contactview, name="contact"),
    path("home/" ,views.homeview , name="home")
]