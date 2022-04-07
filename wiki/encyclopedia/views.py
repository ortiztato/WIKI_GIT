from django.shortcuts import render
from django import forms

from . import util

class busquedaform(forms.Form):
    entradabuscada = forms.CharField(label="Search Encyclopedia")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": busquedaform()
    })

def cargarentry (request, nombre):
    return render(request, "encyclopedia/cargarentry.html", {
        "entry": util.get_entry(nombre),
        "titulo":nombre.upper(),
        "form": busquedaform()
    } )

def busqueda (request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        form = busquedaform(request.POST)
        if form.is_valid():
            entradabuscada = form.cleaned_data["entradabuscada"]
            return render(request, "encyclopedia/cargarentry.html", {
            "entry": util.get_entrybus(entradabuscada),
            "titulo":entradabuscada,
            "form": busquedaform()
    } )