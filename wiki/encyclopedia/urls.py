from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("busqueda", views.busqueda, name="busqueda"),
    path("newpage", views.newpage, name="newpage"),
    path("editentry", views.editentry, name="editentry"),
    path("<str:nombre>", views.cargarentry, name="cargarentry"),
    
]
