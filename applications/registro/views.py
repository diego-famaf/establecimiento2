from typing import AsyncIterable, Generator, Generic, List
from django.shortcuts import render

from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Materia, Empleado, Oficina
"""from .forms import EmpleadoForm"""



# Create your views here.


class EmpleadoListViewAll(ListView):
    model = Empleado
    template_name = 'registro/list_all.html'
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista

class EmpleadoListViewPorDespacho(ListView):
    model = Empleado
    template_name = 'registro/list_por_despacho.html'
    context_object_name = 'despacho'
    
    def get_queryset(self):
        despacho = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            oficina__short_name = despacho
        
        )
        return lista

class EmpleadoListViewPorMateria(ListView):
    model = Empleado
    template_name = 'registro/list_por_materia.html'
    context_object_name = 'asignatura'
    
    def get_queryset(self):
        asignatura = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            materia__short_name = asignatura
        
        )
        return lista


    

class EmpleadoListViewBuscar(ListView):
    model = Empleado
    template_name = 'registro/buscar.html'
    context_object_name = 'lista'

    

class EmpleadoListViewDocente(ListView):
    model = Empleado
    template_name = "registro/list_por_docente.html"
    context_object_name = 'docente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            last_name__icontains = palabra_clave
        ). filter(
             job = '0'
        )
        return lista

        

class EmpleadoListViewNoDocente(ListView):
    model = Empleado
    template_name = "registro/list_por_nodocente.html"
    
    context_object_name = 'nodocente'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            last_name__icontains = palabra_clave
        ). filter(
             job = '1'
        )
        return lista

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'registro/detalle.html'
    context_object_name = 'detalle'



class SuccessView(TemplateView):
    template_name = "registro/exito.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "registro/alta.html"
    fields = [
        "first_name" ,
        "last_name" ,
        "age" ,
        "job" ,
        "materia" ,
        "oficina" ,
        "photo" ,
    ]
    success_url = reverse_lazy('registro_app:listar-todo')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "registro/update.html"
    fields = [
        "first_name" ,
        "last_name" ,
        "age" ,
        "job" ,
        "materia" ,
        "oficina" ,
        "photo" ,
    ]
    success_url = reverse_lazy('registro_app:listar-todo')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)




class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "registro/delete.html"
    success_url = reverse_lazy('registro_app:listar-todo')


class MateriaUpdateView(UpdateView):
    model = Materia
    template_name = "registro/updatemateria.html"
    fields = [
        "name" ,
        "short_name",
    ]
    success_url = reverse_lazy('registro_app:exitomateria')

    def form_valid(self, form):
        materia = form.save(commit=False)
        materia.name = materia.name
        materia.save()
        return super(MateriaUpdateView, self).form_valid(form)    

class MateriaDeleteView(DeleteView):
    model = Materia
    template_name = "registro/delete.html"
    success_url = reverse_lazy('registro_app:exitomateria')


class ESuccessView(TemplateView):
    template_name = "registro/exitomateria.html"

class MateriaCreateView(CreateView):
    model = Materia
    template_name = "registro/altamateria.html"
    fields = [
        "name" ,
        "short_name" ,
        
    ]
    success_url = reverse_lazy('registro_app:listar-materia')

    def form_valid(self, form):
        materia = form.save(commit=False)
        materia.name = materia.name 
        materia.save()
        return super(MateriaCreateView, self).form_valid(form)  

class MateriaListViewMateria(ListView):
    model = Materia
    template_name = 'registro/materias.html'
    context_object_name = 'materia'
    paginate_by = 4


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Materia.objects.filter(
            name__icontains = palabra_clave
        )
        return lista




class OficinaListViewOficina(ListView):
    model = Oficina
    template_name = 'registro/oficinas.html'
    context_object_name = 'oficina'
    paginate_by = 4


    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Oficina.objects.filter(
            name__icontains = palabra_clave
        )
        return lista




class OSuccessView(TemplateView):
    template_name = "registro/exitooficina.html"

        

class OficinaUpdateView(UpdateView):
    model = Oficina
    template_name = "registro/updateoficina.html"
    fields = [
        "name" ,
        "short_name",
    ]
    success_url = reverse_lazy('registro_app:exitooficina')

    def form_valid(self, form):
        oficina = form.save(commit=False)
        oficina.name = oficina.name
        oficina.save()
        return super(OficinaUpdateView, self).form_valid(form)
      

class OficinaCreateView(CreateView):
    model = Oficina
    template_name = "registro/altaoficina.html"
    fields = [
        "name" ,
        "short_name" ,
        
    ]
    success_url = reverse_lazy('registro_app:exitooficina')

    def form_valid(self, form):
        oficina = form.save(commit=False)
        oficina.name = oficina.name 
        oficina.save()
        return super(OficinaCreateView, self).form_valid(form)        

class OficinaDeleteView(DeleteView):
    model = Oficina
    template_name = "registro/delete.html"
    success_url = reverse_lazy('registro_app:exitooficina')


class VistaPrincipal(TemplateView):
    template_name = "index.html"
