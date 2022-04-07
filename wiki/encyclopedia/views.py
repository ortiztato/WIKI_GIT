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

        form = busquedaform(request.POST)  # Take in the data the user submitted and save it as form
        if form.is_valid():
            entradabuscada = form.cleaned_data["entradabuscada"].lower()
            entries = util.list_entries()
            a = (map(lambda x: x.lower(), entries))
            entriesmin = list(a)
            if (entradabuscada in entriesmin):
                    return render(request, "encyclopedia/cargarentry.html", {
                        "entry": util.get_entrybus(entradabuscada),
                        "titulo":entradabuscada.upper(),
                        "form": busquedaform()
                    } )
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
                    "form": busquedaform()
                    } )
    