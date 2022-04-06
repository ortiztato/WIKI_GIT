from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def cargarentry (request, nombre):
    return render(request, "encyclopedia/cargarentry.html", {
        "entry": util.get_entry(nombre),
        "titulo":nombre.upper()
    } )