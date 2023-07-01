from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("icecream",views.icecream,name='icecream'),
    # path("softy",views.softy,name='softy'),
    # path("familypack",views.familypack,name='familypack')
]