from ctypes import sizeof
from xml.dom.minidom import AttributeList
from django.shortcuts import render
from django import forms
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from . import util



class busquedaform(forms.Form):
    entradabuscada = forms.CharField(label="Search Encyclopedia")

class newpageform(forms.Form):
    titulonewpage = forms.CharField(label="Complete Entry Title")
    cuerponewpage = forms.CharField(label="",
        widget=forms.Textarea(attrs={'placeholder': "cuerpo del entry", 'width':10}))
    

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
                listaresultados = []
                for entry in entriesmin:    
                    if entradabuscada in entry:
                        listaresultados.append(entry)
            return render(request, "encyclopedia/resultados.html", {
                    "entries": listaresultados,
                    "form": busquedaform()
    })
def newpage (request):
    if request.method == "POST":

        form = newpageform(request.POST)
        if form.is_valid():
            titulonewpage = form.cleaned_data["titulonewpage"].lower()
            content = form.cleaned_data["cuerponewpage"].lower()
            filename = f"entries/{titulonewpage}.md"
            if default_storage.exists(filename):
                return render(request, "encyclopedia/errorentrada.html", {
                    "form": busquedaform()})
            else: 
                default_storage.save(filename, ContentFile(content))
                return render(request, "encyclopedia/cargarentry.html", {
                    "entry": util.get_entry(titulonewpage),
                    "titulo":titulonewpage.upper(),
                    "form": busquedaform()
    } )
    return render(request, "encyclopedia/newpage.html", {
        "formtitulo": newpageform(),
        "form": busquedaform()
    })

def editentry (request, nombre):
    titulonewpage = forms.CharField(label="Complete Entry Title", initial=nombre)
    return render(request, "encyclopedia/editentry.html", {
        "formtitulo": newpageform(),
        "form": busquedaform()
    } )
