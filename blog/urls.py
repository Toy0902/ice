from django.urls import path
from .views import *
urlpatterns =[
    path('',index,name='index'),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('gallery/', gallery, name="gallery"),
    path('product/', product, name="product"),
    path('service/', service, name="service"),
]