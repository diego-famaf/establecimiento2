from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'registro_app'

urlpatterns = [
    path(
        'listar-todo/', 
        views.EmpleadoListViewAll.as_view(),
        name='listar-todo'
    ),
    path(
        'listar-por-despacho/<short_name>/', 
        views.EmpleadoListViewPorDespacho.as_view(), 
        name='listar-por-despacho'
    ),
    path(
        'listar-por-materia/<short_name>/', 
        views.EmpleadoListViewPorMateria.as_view(), 
        name='listar-por-asignatura'
    ),    
    path(
        'listar-materias/', 
        views.MateriaListViewMateria.as_view(), 
        name='listar-materias'

    ),
    path(
        'listar-oficinas/', 
        views.OficinaListViewOficina.as_view(), 
        name='listar-oficinas'

    ),
    path(
        'listar-por-apellido/', 
        views.EmpleadoListViewBuscar.as_view(),
        name='buscar'


    ),
    path(
        "listar-por-docente/",
        views.EmpleadoListViewDocente.as_view(),
        name="listar-por-docente"
    ),
    path(
        "listar-por-nodocente/",
        views.EmpleadoListViewNoDocente.as_view(),
        name="listar-por-nodocente"
    ),
    path(
        'detalle/<pk>/',
        views.EmpleadoDetailView.as_view(),
        name='detalle'
    ),
    path(
        "exito/",
        views.SuccessView.as_view(),
        name="exito"
    ),
    path(
        "exitomateria/",
        views.ESuccessView.as_view(),
        name="exitomateria"
    ),
    path(
        "exitooficina/",
        views.OSuccessView.as_view(),
        name="exitooficina"
    
    ),
    path(
        "alta/<pk>/",
        views.EmpleadoCreateView.as_view(),
        name="alta"
    ),

    path(
        "altaoficina/<pk>/",
        views.OficinaCreateView.as_view(),
        name="altaoficina"
    ),
    path(
        "altamateria/<pk>/",
        views.MateriaCreateView.as_view(),
        name="altamateria"

    ),
    path(
        "update/<pk>/", 
        views.EmpleadoUpdateView.as_view(),
        name="update"
    ),
    path(
        "updatemateria/<pk>/", 
        views.MateriaUpdateView.as_view(),
        name="updatemateria"
    ),
    path(
        "updateoficina/<pk>/", 
        views.OficinaUpdateView.as_view(),
        name="updateoficina"
    ),
    path(
        "delete/<pk>/", 
        views.EmpleadoDeleteView.as_view(),
        name="delete"
    ),   
    path(
        "deletemateria/<pk>/", 
        views.MateriaDeleteView.as_view(),
        name="deletemateria"
    ), 
    path(
        "deleteoficina/<pk>/", 
        views.OficinaDeleteView.as_view(),
        name="deleteoficina"
    ), 
    path(
        "", 
        views.VistaPrincipal.as_view(), 
        name="index"
    ),
]

