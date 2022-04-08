from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("busqueda", views.busqueda, name="busqueda"),
    path("newpage", views.newpage, name="newpage"),
    path("wiki/<str:titulo>/edit", views.editentry, name="editentry"),
    path("wiki/<str:entry>", views.cargarentry, name="cargarentry"),
    path("random", views.random, name="random"),
    
]
